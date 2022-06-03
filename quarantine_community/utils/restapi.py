from utils import api2df, do_supply_static
from utils import special_request_url, supply_request_url

if __name__ == '__main__':
    supply_df = api2df(supply_request_url, '必需品需求')
    do_supply_static(supply_df, '必需品需求')
    special_df = api2df(special_request_url, '特殊需求', special_req=True)
    # do_supply_static(special_df, '特殊需求', special_req=True)
