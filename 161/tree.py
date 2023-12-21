import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    



    def count(directory):


        num_files = num_dirs = 0


        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory,file)):
                num_files += 1
            elif os.path.isdir(os.path.join(directory,file)):
                num_dirs += 1

                dirs,files = count(os.path.join(directory,file))
                num_dirs += dirs
                num_files += files


        return num_dirs,num_files




    return count(directory)    
    


