class Employee:
    def __init__ (
            self,
            designation : str = 'Developer',
            frontend : bool = True,
            backend : bool = True
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__ (self):
        return '{}'.format (self.designation, self.frontend, self.backend)
    
    ### Write the your method over here.
    def verifier (self):
        if self.frontend and self.backend:
            return 'Full Stack Developer'
        elif self.frontend : 
            return 'Front End Developer'
        elif self.backend :
            return 'Back End Developer'
        else :
            return 'NULL'

if __name__ == '__main__':
    firstEmployee = Employee ()
    print (firstEmployee.verifier());