"""Module containing the elementary particle classes. """

import numpy as np


class ElementaryParticle:
    """ Elementary particle class.

    Attributes
    ----------
    x : float
        x-position of the particle.

    y: float
        y-position of the particle.

    ptype: str
        Statistics obeyed by the particle.

    charge : float
        Electric charge of the particle.

    mass : float
        Rest mass in MeV of the particle.

    spin: float
        Spin of the particle.
        

    Methods
    -------
    info():
        Prints particles information.

    is_antiparticle(other):
        Check if the other is this particle anti-particle

    move()
        Move the particle randomly.

    place_at(coord):
        Place the particle at passed coord.
        
    check_type():
        Check whether particle is a boson or fermion.
        
    """

    x = None
    y = None

    def __init__(self, charge, mass, spin, ptype = None):
        """Initialize the particle's attributes.

        Parameters
        ----------
        charge : float
            Electric charge of the particle.

        mass : float
            Rest mass in MeV of the particle.

        spin: float
            Spin of the particle.

        """
        self.charge = charge
        self.mass = mass
        self.spin = spin

    def info(self):
        """Print to scree information about the particle."""

        print(f"The particle has a mass of {self.mass} MeV")
        print(f"The particle's charge is {self.charge} e")
        print(f"The particle's spin is {self.spin}")

    def place_at(self, coord):
        """Place particles at coordinates (x,y).

        Parameters
        ----------
        coord: tuple
            (x,y) coordinates where to place the particle.
        """
        self.x = coord[0]
        self.y = coord[1]

    def move(self):
        """Move the particle by randomly pushing it in both directions."""
        self.x += np.random.randint(low=-1, high=2)
        self.y += np.random.randint(low=-1, high=2)
        
        
    def check_type(self):
        """Checks particle spin to determine particle type. Integer spin rates
        indicate a bosun, while fractional spin rates indicate a fermion."""
        if self.spin.is_integer() == True:
            self.ptype = "bosun"
        else:
            self.ptype = "fermion"
        return self.ptype
    
    def compare(self, other):
        """Compares particle attributes, produces true/false output. Takes in
        the elementary particle and then the other particle."""
        if isinstance (other, ElementaryParticle):
            print("The two particles have the same charge:", (self.charge == other.charge))
            print("The two particles have the same mass:", (self.mass == other.mass))
            print("The two particles have the same spin:", (self.spin == other.spin))
        
        else:
            raise ValueError("You need to pass a valid particle!")
            