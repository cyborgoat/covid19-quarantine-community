from util.stat import api2df, do_supply_static
from util.stat import special_request_url, supply_registration_url

if __name__ == '__main__':
    supply_df = api2df(supply_registration_url, '必需品需求')
    do_supply_static(supply_df, '必需品需求')
    special_df = api2df(special_request_url, '特殊需求', special_req=True)
    # do_supply_static(special_df, '特殊需求', special_req=True)
