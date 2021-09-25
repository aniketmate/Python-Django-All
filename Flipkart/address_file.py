from parent_file import Base

class Address(Base):
    """ADDRESS DETAILS"""
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
    ad_obj = Address("21-B", "Kalamboli", 410218, "Panvel", "Maharashtra")
    ad_obj1 = Address("41-B", "Vashi", 400718, "Navi Mumbai", "Maharashtra")

    print(ad_obj)
    ad_obj.show_address()

