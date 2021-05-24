import amiet_tools as AmT
import json
import os


def loadTestSetup(*args):
    """
    Load test variable values for calculations, either from default values or
    from a given .txt test configuration setup file. File must contain the
    following variable values, in order:

        c0                  speed of sound [m/s]
        rho0                density of air [kg/m**3]
        p_ref               reference pressure [Pa RMS]
        Ux                  mean flow velocity [m/s]
        turb_intensity      turbulent flow intensity [ = u_rms/Ux]
        length_scale        turbulence integral length scale [m]
        z_sl                shear layer height (from aerofoil)

    Empty lines and 'comments' (starting with '#') are ignored.

    path_to_file: str [Optional]
        Relative path to setup file
    """

    # if called without path to file, load default testSetup (DARP2016)
    if len(args) == 0:
        return AmT.TestSetup()

    else:
        name, extension = os.path.splitext(args[0])
        if extension == ".json":
            with open(args[0], encoding="utf-8") as f:
                obj = json.load(f)
                f.close()

            tS = AmT.TestSetup(c0=obj["c0"], rho0=obj["rho0"],
                               p_ref=obj["Ux"], Ux=obj["Ux"],
                               turb_intensity=obj["turb_intensity"],
                               length_scale=obj["length_scale"],
                               z_sl=obj["z_sl"])

            return tS
        elif extension == ".txt":
            # initialize new instance of testSetup
            testSetupFromFile = AmT.TestSetup()

            varList = ['c0', 'rho0', 'p_ref', 'Ux', 'turb_intensity',
                       'length_scale', 'z_sl']
            i = 0

            # open file name given by 'args[0]'
            with open(args[0]) as f:
                # get list with file lines as strings
                all_lines = f.readlines()

                # for each line...
                for line in all_lines:

                    # skip comments and empty lines
                    if line[0] in ['#', '\n']:
                        pass

                    else:
                        words = line.split('\t')
                        # take 1st element as value (ignore comments)
                        exec('testSetupFromFile.' +
                             varList[i] + '=' + words[0])
                        i += 1

            return testSetupFromFile
        else:
            raise ValueError("{} is not a valid format".format(extension))


def loadAirfoilGeom(*args):
    """
    Load airfoil geometry values for calculations, either from default values or
    from a given .json airfoil geometry file. File must contain the
    following variable values, in order:

        b       Airfoil semichord [m]
        d       Airfoil semispan [m]
        Nx      Number of chordwise points (non-uniform sampling)
        Ny      Number of spanwise points (uniform sampling)

    Empty lines and 'comments' (starting with '#') are ignored.

    path_to_file: str [Optional]
        Relative path to airfoil geometry file
    """

    # if called without path to file, load default geometry (DARP2016)
    if len(args) == 0:
        return AmT.AirfoilGeom()

    else:
        name, extension = os.path.splitext(args[0])
        if extension == ".json":
            with open(args[0], encoding="utf-8") as f:
                obj = json.load(f)
                f.close()

            # initialize new instance of testSetup
            aG = AmT.AirfoilGeom(b=obj["b"], d=obj["d"],
                                 Nx=obj["Nx"], Ny=obj["Ny"])

            return aG
        elif extension == ".txt":
            # initialize new instance of testSetup
            airfoilGeomFromFile = AmT.AirfoilGeom()

            varList = ['b', 'd', 'Nx', 'Ny']
            i = 0

            #path_to_file = '../DARP2016_AirfoilGeom.txt'
            with open(args[0]) as f:
                # get list with file lines as strings
                all_lines = f.readlines()

                # for each line...
                for line in all_lines:

                    # skip comments and empty lines
                    if line[0] in ['#', '\n']:
                        pass

                    else:
                        words = line.split('\t')
                        # take 1st element as value (ignore comments)
                        exec('airfoilGeomFromFile.' +
                             varList[i] + '=' + words[0])
                        i += 1


            return airfoilGeomFromFile

        else:
            raise ValueError("{} is not a valid format".format(extension))
