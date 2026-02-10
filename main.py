import pandas as pd
import re

df = pd.read_csv('csv/vEdge-02-10-2026.csv')
df = df.get(['Hostname', 'Version', 'Reachability', 'Subject SUDI serial #'])
print(df)
print('\n')
router_LA = []
dc_drc_LA_pattern = "(^DC|DRC).*(LA|LA\\d+)$"

router_TLK = []
dc_drc_TLK_pattern = "(^DC|DRC).*(TLK|TLK\\d+)$"

router_PINS = []
dc_drc_PINS_pattern = "(^DC|DRC).*(PINS|PINS\\d+)$"

version_pattern = "17\\.12.*"

for row in df.itertuples(index=False):
    hostnames = row[0]
    version = row[1]
    status = row[2]
    if isinstance(hostnames, float) == False and re.match(version_pattern, str(version), flags=0) and status == 'reachable':
        match = re.match(dc_drc_LA_pattern, hostnames, flags=0)
        if match:
            result = {
                'hostname': row[0],
                'version': row[1],
                'SN': row[3]
            }
            router_LA.append(result)
            # print(hostnames)

print(f'Total Router LA: {len(router_LA)}')
router_LA_df = pd.DataFrame(data=router_LA)
print(router_LA_df)
router_LA_df.to_csv(path_or_buf='output/3.csv',index=False, mode='x')