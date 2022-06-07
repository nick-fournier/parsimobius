from webgui.models import OD, RAC, WAC
from lodes_star.fetch import fetch_lodes
import tqdm

def store_lodes(lodes_dict):
    for table_name, df in lodes_dict.items():
        table_type = [x.upper() for x in ['od', 'rac', 'wac'] if x in table_name][0]
        print('Storing ' + table_name + ' in ' + table_type)
        if not globals()[table_type].objects.filter(table_name=table_name).exists():
            objs = [
                globals()[table_type](
                    **{
                        **row.to_dict(),
                        **{'year': row['createdate'],
                           'table_name': table_name}
                    }
                )
                for index, row in df.iterrows()
            ]
            globals()[table_type].objects.bulk_create(objs)
    print('Done')

if __name__ == "__main__":
    lodes_data = fetch_lodes(state='ma', zone_types=['od', 'rac', 'wac'], year='2019', cache=True)
    store_lodes(lodes_data)
