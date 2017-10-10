# Classic Kinetic Energy Calculator

# Kinetic Energy Function
def K_Energy(Mass,Speed):
    
    
     
    # Input mass converted to floating point number, make positive if not already.    
    try:
        MassFloat = float(Mass);
        if MassFloat < 0:
            MassFloat = abs(MassFloat);
            print("Negative mass corrected.");
        if MassFloat == 0:
            print("Mass must be non-zero");
            return
    except:
        print("Mass must be a numeric value.");
        return


    # Input speed converted to floating point number. 
    try:
        SpeedFloat = float(Speed);
    except:
        print("Speed must be a numeric value.");
        return
    
    
    # Calculates speed squared
    SqrSpeed = SpeedFloat**2;
    
    # Calculates kinetic energy T = 1/2 * m * v^2
    T = 0.5*MassFloat*SqrSpeed;
    
    # Print results, export value for further use.
    print("A particle of mass %6.3f kg moving at a speed %6.3f m/s has a translational kinetic energy of %7.3f J" % (MassFloat,SpeedFloat,T));
    return T;
        


# Function Test
# Define variables
m = 0;
v = 2;

# Run function, defining answer as T for later use
T = K_Energy(m,v);
