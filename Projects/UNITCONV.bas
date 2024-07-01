DECLARE SUB ConvertUnits (unit1$, unit2$, factor!)
DECLARE SUB DisplayMenu ()
DECLARE SUB GetValidChoice (choice%)
DECLARE SUB ProcessChoice (choice%)

DIM choice AS INTEGER

CLS
PRINT "Welcome to the Enhanced Unit Converter"
PRINT "======================================="

DO
    CALL DisplayMenu
    CALL GetValidChoice(choice)
    CALL ProcessChoice(choice)
    IF choice <> 7 THEN
        PRINT
    END IF
LOOP WHILE choice <> 7

PRINT "Program Exited"
END

SUB DisplayMenu ()
    PRINT "1. Convert meters to centimeters"
    PRINT "2. Convert centimeters to meters"
    PRINT "3. Convert meters to inches"
    PRINT "4. Convert inches to meters"
    PRINT "5. Convert centimeters to inches"
    PRINT "6. Convert inches to centimeters"
    PRINT "7. Exit"
    PRINT "======================================="
END SUB

SUB GetValidChoice (choice%)
    DO
        INPUT "Choose an option (1-7): ", choice%
        IF choice% < 1 OR choice% > 7 THEN
            PRINT "Invalid option. Please choose between 1 and 7."
        END IF
    LOOP UNTIL choice% >= 1 AND choice% <= 7
END SUB

SUB ProcessChoice (choice%)
    SELECT CASE choice%
        CASE 1
            CALL ConvertUnits("meters", "centimeters", 100!)
        CASE 2
            CALL ConvertUnits("centimeters", "meters", .01!)
        CASE 3
            CALL ConvertUnits("meters", "inches", 39.3701!)
        CASE 4
            CALL ConvertUnits("inches", "meters", .0254!)
        CASE 5
            CALL ConvertUnits("centimeters", "inches", .393701!)
        CASE 6
            CALL ConvertUnits("inches", "centimeters", 2.54!)
        CASE 7
            PRINT "Exiting the program. Goodbye!"
    END SELECT
END SUB

SUB ConvertUnits (unit1$, unit2$, factor!)
    DIM value AS DOUBLE
    DIM result AS DOUBLE
    DO
        PRINT "Enter value in "; unit1$; ": "
        INPUT "", value
        IF value < 0 THEN
            PRINT "Please enter a positive value."
        END IF
    LOOP UNTIL value >= 0
    
    result = value * factor!
    PRINT USING "###.######"; value;
    PRINT " "; unit1$; " is ";
    PRINT USING "###.######"; result;
    PRINT " "; unit2$
END SUB
