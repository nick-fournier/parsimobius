from webgui.models import *
from lodes_star.fetch import fetch_lodes
from lodes_star.state_codes import State


def store_lodes(lodes_dict):
    #TODO place fetch in the loop, check if state has been stored, if not download it.
    for filename, df in lodes_dict.items():
        keys = filename.split('_')
        table_name = '_'.join(keys[1:5]).upper()

        if globals()[table_name].objects.filter(state=keys[0]).count() == 0:
            print('Storing ' + filename + ' in ' + table_name)
            objs = [
                globals()[table_name](
                    **{
                        **row.to_dict(),
                        **{'state': keys[0]}
                    }
                )
                for index, row in df.iterrows()
            ]
            globals()[table_name].objects.bulk_create(objs)
        else:
            print('Skipping ' + table_name + '. Already contains data!')


if __name__ == "__main__":
    states = [x for x in State.abb2name.keys() if x not in ['AS', 'GU', 'MP', 'PR', 'VI', 'UM']]
    for state in states:
        lodes_dict = fetch_lodes(state=state, zone_types=['od', 'rac', 'wac'], year='2019', cache=True)
        # store_lodes(lodes_dict)
