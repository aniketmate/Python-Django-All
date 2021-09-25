from parent_file import Parent

class Address(Parent):
    """ADDRESS DETAILS"""
    addr_list = []
    def __init__(self, house_no, area, pin, city, state):
        self.AddrHouse = house_no
        self.AddrArea = area
        self.AddrPin = pin
        self.AddrCity = city
        self.AddrState = state

    def show_address(self):
        """SHOW ADDRESS"""
        return (f"""
            -------ADDRESS-------
        House No:- {self.AddrHouse}
        Area:-{self.AddrArea}
        Pin:-{self.AddrPin}
        City:-{self.AddrCity}
        State:-{self.AddrState}
        
        """)


if __name__ == '__main__':


    ad_obj1 = Address("18-1004", "Kalamboli", 410218, "Panvel", "Maharashtra")
    ad_obj2 = Address("17", "Koperkhairne", 400709, "Navi Mumbai", "Maharashtra")
    ad_obj3 = Address("8", "Vashi", 400703, "Navi Mumbai", "Maharashtra")
    ad_obj4 = Address("PL-31", "New Panvel", 410206, "Panvel", "Maharashtra")
    ad_obj5 = Address("KL-55", "Roadpali", 410219, "Panvel", "Maharashtra")



    Address.addr_list.append([ad_obj1,ad_obj2,ad_obj3,ad_obj4,ad_obj5])
    # print(Address.addr_list)

