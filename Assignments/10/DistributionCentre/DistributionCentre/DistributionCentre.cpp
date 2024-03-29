// DistributionCentre.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

#define PI 3.141593

using namespace std;


struct settlement {
	//string name;
	//double type;
	double population;
	double latitude;
	double longitude;
};

double haversineDistance(settlement Loc1, settlement Loc2);




int main() {

	///
	/// Import data as an array structure
	///
	//string fileName;
	//cout << "Which file would you like to load (use full file name)?\n";
	//cin >> fileName;
	//ifstream dataFile(fileName);										// Load file which has been selected  
	ifstream dataFile("GBplaces.csv");

	settlement listedSettlements[100];

	if (dataFile.is_open()) {
		cout << "File opened successfully\n";
		string aLine;
		int i = -2;
		double degToRad = (PI / 180);

		while (!dataFile.eof()) {										// Add elements to data structure
			getline(dataFile, aLine);									// Take line from file as a string
			i++;

			if ((aLine.length() > 0) && (i != -1)) {
				int prevComma = -1;										// Define comma positions
				int Comma;
				string dataHolder[5];

				for (int j = 0; j < 5; j++) {
					Comma = aLine.find(',', prevComma + 1);				// Find the position of the next comma
					dataHolder[j] = aLine.substr(prevComma + 1, Comma);	// Take the string between the previous comma and the next comma
					prevComma = Comma;									// Set previous comma as current comma
				}

				dataHolder[4] = aLine.substr(prevComma + 1, aLine.length());	// Add last string to temporary vector

				cout << i << ": " << aLine << "\n  " << dataHolder[0] << " || " << dataHolder[1] << " || " << dataHolder[2] << " || " << dataHolder[3] << " || " << dataHolder[4] << "\n";
				listedSettlements[i].population = atof(dataHolder[2].c_str());
				listedSettlements[i].latitude = atof(dataHolder[3].c_str())*degToRad;
				listedSettlements[i].longitude = atof(dataHolder[4].c_str())*degToRad;
			}
		}
	}

	else {
		cout << "File could not be opened or does not exist\n";
		exit(1);
	}

	///
	///
	///



	return 0;
}





double haversineDistance(settlement Loc1, settlement Loc2) {



	double dLat = Loc2.latitude - Loc1.latitude;
	double dLong = Loc2.longitude - Loc1.longitude;

	double a = pow(sin(0.5*dLat), 2) + cos(Loc1.latitude)*cos(Loc2.latitude)*pow(sin(0.5*dLong), 2);
	double c = 2 * asin(pow(a, 0.5));
	double dist = 6371 * c;

	return dist;




}