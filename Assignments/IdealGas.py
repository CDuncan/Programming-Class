# Ideal Gas Law Calculator



print("This program allows you calculate properties of a gas using the ideal gas law.\n")
R = 8.315;


# Allow more calculations
Calculate = 1;
while Calculate == 1:
    
    # Records which of the quantities have been assigned values
    State = [0,0,0];

    # Inputs
    while sum(State) != 2:
        Selection = input("Would you like to enter a: [p]ressure, [t]emperature, or [v]olume?\n").lower();
    
        if Selection == "p":
            Pressure = input("Please enter the pressure in Pascals: ");
            try:
                PressureFloat = float(Pressure);
                # Disqualify sub zero values, log that a value has been given for a quantity
                if PressureFloat > 0:
                    State[0] = 1;
                else:
                    print("Pressure must be positive and non zero.\n");
            except:
                print("Pressure must be a numeric value.\n")
    
        elif Selection == "t":
            Temperature = input("Please enter the temperature in Kelvin: ");
            try:
                TemperatureFloat = float(Temperature);
                if TemperatureFloat > 0:
                    State[1] = 1;
                else:
                    print("Temperature must be positive and non zero.\n");
            except:
                print("Temperature must be a numeric value.\n");

        elif Selection == "v":
            Volume = input("Please enter the volume in m^3: ");
            try:
                VolumeFloat = float(Volume);
                if VolumeFloat > 0:
                    State[2] = 1;
                else:
                    print("Volume must be positive and non zero.\n");
            except:
                print("Volume must be a numeric value.\n");
    
        else:
            print("Sorry, I do not understand that input.\n");


    # Calculations
    if State == [1,1,0]:
        # P and T provided
        # V = RT/P
        VolumeFloat = R*TemperatureFloat/PressureFloat;
        print("For a molar gas with temperature %5.2f K and pressure %5.2e Pa, the volume is %5.2e m^3" % (TemperatureFloat,PressureFloat,VolumeFloat));

    elif State == [1,0,1]:
        # P and V provided
        # T = PV/R
        TemperatureFloat = PressureFloat*VolumeFloat/R;
        print("For a molar gas with pressure %5.2e Pa and volume %5.2e m^3, the temperature is %5.2f K" % (PressureFloat,VolumeFloat,TemperatureFloat));
   
    elif State == [0,1,1]:
        # V and T provided
        # P = RT/V
        PressureFloat = R*TemperatureFloat/VolumeFloat;
        print("For a molar gas with temperature %5.2f K and volume %5.2e m^3, the pressure is %5.2e Pa" % (TemperatureFloat,VolumeFloat,PressureFloat));    
    
    ValidAnswer = 0;
    while ValidAnswer == 0:
        Cont = input("Would you like you to perform another calculation? (y/n)\n").lower();
        if Cont == "y":
            ValidAnswer = 1;
        elif Cont == "n":
            ValidAnswer = 1;
            Calculate = 0;
            print("Thank you for using me.\n");
        else:
            print("Sorry, I do not understand that input.\n");

