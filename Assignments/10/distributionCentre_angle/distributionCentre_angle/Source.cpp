// distributionCentre_angle.cpp : Defines the entry point for the console application.
//


// Packages
#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <sstream>

// Definitions
#define PI 3.141593
//#define NAN "thefuckdoiknowaboutcoding"

// Settings
using namespace std;

// Structures
struct position {
	double latitude;
	double longitude;
};
struct point {
	int number;
	position pos;
	vector <double> relDistance;
	double angle;
	double relPopulation;
	double demand;
};

// Functions
vector<string> getNextLineAndSplitIntoTokens(istream& str);
double haversineDistance(point Loc1, point Loc2);
vector<double> relativeDistance(vector <point> List, int i);
bool sortByAngle(point i, point j);


int main() {
	point baseLocation;
	baseLocation.number = 0;
	baseLocation.pos.latitude = 0.938247293;
	baseLocation.pos.longitude = -0.025824677;
	baseLocation.angle = 0;
	baseLocation.relPopulation = 0;
	
	/// Import data as a vector structure

	//string fileName;
	//cout << "Which file would you like to load (use full file name)?\n";
	//cin >> fileName;
	//ifstream dataFile(fileName);										// Load file which has been selected  
	ifstream dataFile("GBplaces.csv");
	vector <point> placeList;

	if (dataFile.is_open()) {
		cout << "File loaded successfully\n";
		vector <string> list;
		point dataPoint;
		placeList.push_back(baseLocation);
		double degToRad = (PI / 180);
		int count = 1;
		while (!dataFile.eof()) {										// Add elements to data structure
			list = getNextLineAndSplitIntoTokens(dataFile);
			dataPoint.number		= count++;
			dataPoint.relPopulation = ceil(stoi(list[2].c_str()) / 100000);		dataPoint.demand = dataPoint.relPopulation;
			dataPoint.pos.latitude	= atof(list[3].c_str())*degToRad;			dataPoint.pos.longitude = atof(list[4].c_str())*degToRad;
			dataPoint.angle			= atan2((dataPoint.pos.latitude - baseLocation.pos.latitude),(dataPoint.pos.longitude - baseLocation.pos.longitude));
			placeList.push_back(dataPoint);

		}
		dataFile.close();

	}
	else {
		cout << "File could not be opened or does not exist\n";
		exit(1);
	}

	sort(placeList.begin(), placeList.end(), sortByAngle);

	for (int i = 0; i < placeList.size(); i++) {
		cout << placeList[i].number << ": " << placeList[i].demand << " Units, " << placeList[i].pos.latitude << "," << placeList[i].pos.longitude << ", " << placeList[i].angle;
	}




	//vector <point> pointList;
	//int number = 0;

	//for (int i = 0; i < placeList.size(); i++) {
		//double relativePop = placeList[i].relPopulation );
		//point tempPoint;
		//for (int j = 0; j < relativePop + 1; j++) {
			//tempPoint.number = number++;
			//tempPoint.pos = placeList[i].pos;
			//pointList.push_back(tempPoint);

		//}
	//}

	// Give each point a distance to each other point
	//for (int i = 0; i < pointList.size(); i++) {
		//pointList[i].relDistance = relativeDistance(pointList, i);
		//double startDistance = haversineDistance(pointList[i], testLocation);
		//pointList[i].relDistance.push_back(startDistance);
		//cout << pointList[i].number << ": " << pointList[i].relDistance.back() << "\n";
	//}















	return 0;
}









vector<string> getNextLineAndSplitIntoTokens(istream& str) {
	vector<string>			result;
	string					line;
	getline(str, line);

	stringstream lineStream(line);
	string					cell;

	while (getline(lineStream, cell, ','))
	{
		result.push_back(cell);
	}
	// This checks for a trailing comma with no data after it.
	if (!lineStream && cell.empty())
	{
		// If there was a trailing comma then add an empty element.
		result.push_back("");
	}
	return result;
}
double haversineDistance(point Loc1, point Loc2) {



	double dLat = Loc2.pos.latitude - Loc1.pos.latitude;
	double dLong = Loc2.pos.longitude - Loc1.pos.longitude;

	double a = pow(sin(0.5*dLat), 2) + cos(Loc1.pos.latitude)*cos(Loc2.pos.latitude)*pow(sin(0.5*dLong), 2);
	double c = 2 * asin(pow(a, 0.5));
	double dist = 6371 * c;

	return dist;


}
vector<double> relativeDistance(vector <point> List, int i) {

	vector <double> distanceVector;
	double distance;
	//  List.size() -1
	for (int j = 0; j < List.size(); j++) {
		distance = haversineDistance(List[i], List[j]);
		distanceVector.push_back(distance);

	}
	return distanceVector;
}
bool sortByAngle(point i, point j) { return (i.angle>j.angle); }
