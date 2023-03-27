import os

# Return list of paths to .pv files
def getPvPaths():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    train_path = os.path.join(cur_path, '../train')

    # Get year names
    years = os.listdir(train_path)
    years.pop() # remove txt

    path_list = []

    for year in years:
        year_path = os.path.join(train_path, year)
        
        # Get person names
        persons = os.listdir(year_path)
        persons.pop() # remove txt

        for person in persons:
            person_path = os.path.join(year_path, person)
            
            for file in os.listdir(person_path):
                if file.endswith('.pv'):
                    path_list.append(os.path.join(person_path, file[:-3]))
        
    return path_list

def makePvList(pv_path):
    f = open(pv_path, 'r')
    pv_list = [round(float(line.rstrip('\n'))) for line in f]
    f.close()
    
    return pv_list

if __name__ == "__main__":
    path_names = getPvPaths()
    pv_path = path_names[0] + '.pv'
    print(makePvList(pv_path))
