import re
import pandas as pd

class BCS:
    def __init__(self):
        pass

    def getLintasartaRouter(dataframe):
        df = dataframe
        df = df.get(['Hostname', 'Version', 'Reachability', 'Subject SUDI serial #'])
        print(df)
        router_LA = []
        dc_drc_LA_pattern = "(^DC|DRC).*(LA|LA\\d+)$"

        for row in df.itertuples(index=False):
            hostnames = row[0]
            status = row[2]
            if isinstance(hostnames, float) == False and status == 'reachable':
                match = re.match(dc_drc_LA_pattern, hostnames, flags=0)
                if match:
                    result = {
                        'hostname': row[0],
                        'version': row[1],
                        'SN': row[3]
                    }
                    router_LA.append(result)
        router_LA_df = pd.DataFrame(data=router_LA)
        print(router_LA_df)
        print(f'Total Router LA: {len(router_LA)}')

    def getTelkomRouter(dataframe):
        df = dataframe
        df = df.get(['Hostname', 'Version', 'Reachability', 'Subject SUDI serial #'])
        print(df)
        router_TLK = []
        dc_drc_TLK_pattern = "(^DC|DRC).*(TLK|TLK\\d+)$"

        for row in df.itertuples(index=False):
            hostnames = row[0]
            status = row[2]
            if isinstance(hostnames, float) == False and status == 'reachable':
                match = re.match(dc_drc_TLK_pattern, hostnames, flags=0)
                if match:
                    result = {
                        'hostname': row[0],
                        'version': row[1],
                        'SN': row[3]
                    }
                    router_TLK.append(result)
        router_TLK_df = pd.DataFrame(data=router_TLK)
        print(router_TLK_df)
        print(f'Total Router Telkom: {len(router_TLK)}')   

    def getPINSRouter(dataframe):
        df = dataframe
        df = df.get(['Hostname', 'Version', 'Reachability', 'Subject SUDI serial #'])
        print(df)
        router_PINS = []
        dc_drc_PINS_pattern = "(^DC|DRC).*(PINS|PINS\\d+)$"

        for row in df.itertuples(index=False):
            hostnames = row[0]
            status = row[2]
            if isinstance(hostnames, float) == False and status == 'reachable':
                match = re.match(dc_drc_PINS_pattern, hostnames, flags=0)
                if match:
                    result = {
                        'hostname': row[0],
                        'version': row[1],
                        'SN': row[3]
                    }
                    router_PINS.append(result)
        router_PINS_df = pd.DataFrame(data=router_PINS)
        print(router_PINS_df)
        print(f'Total Router PINS: {len(router_PINS)}')

    def getUpgradedRouter(dataframe):
        df = dataframe
        df = df.get(['Hostname', 'Version', 'Reachability', 'Subject SUDI serial #'])
        print(df)
        upgraded_router = []
        version_pattern = "17\\.12.*"

        for row in df.itertuples(index=False):
            hostnames = row[0]
            version = row[1]
            status = row[2]
            if isinstance(hostnames, float) == False and re.match(version_pattern, str(version), flags=0) and status == 'reachable':
                match = re.match(version_pattern, str(version), flags=0)
                if match:
                    result = {
                        'hostname': row[0],
                        'version': row[1],
                        'SN': row[3]
                    }
                    upgraded_router.append(result)
        upgraded_router_df = pd.DataFrame(data=upgraded_router)
        print(upgraded_router_df)
        print(f'Total of Upgraded Router: {len(upgraded_router)}')