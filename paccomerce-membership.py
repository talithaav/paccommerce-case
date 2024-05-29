# import library
from tabulate import tabulate
from math import sqrt

class Membership:
    
    # insert dummy data
    data = {'Sumbul': 'Platinum', 'Ana': 'Gold', 'Cahya': 'Platinum'}
    
    def __init__(self, username):
        self.username = username
        
    def show_benefit(self):
        """
        Function to show all PacCommerce Membership Benefit Table.
        """
        headers = ['Membership', 'Discount', 'Another Benefit']
        
        table = [['Platinum', '15%', 'Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%'],
                 ['Gold', '10%', 'Benefit Silver + Voucher Ojek Online'],
                 ['Silver', '8%', 'Voucher Makanan']]
        
        print('Benefit Membership PacCommerce\n')
        print(tabulate(table, headers=headers, tablefmt='fancy_grid', stralign="center"))
        
    def show_requirements(self):
        """
        Function to show all Requirements Membership PacCommerce Table.
        """
        headers = ['Membership', 'Monthly Expense (juta)', 'Monthly Income (juta)']
        
        table = [['Platinum', 8, 15],
                 ['Gold', 6, 10],
                 ['Silver', 5, 7]]
        
        print('Requirements Membership PacCommerce\n')
        print(tabulate(table, headers=headers, tablefmt='fancy_grid', stralign="center"))
        
    def predict_membership(self, username, monthly_expense, monthly_income):
        """
        Function to predict user's membership based on their monthly expense and monthly income by using Euclidean Distance approach.
        
        Parameters
        ----------
        username: string
            input username
        monthly_expense: int
            expenses spent by users every month
        monthly income: int
            income earned by users every month
        """
        memb_parameter = [[8, 15], [6, 10], [5,7]]
        
        result = []
        for idx, _ in enumerate(memb_parameter):
            euclidean = round(sqrt((monthly_expense - memb_parameter[idx][0])**2 + \
                                   (monthly_income - memb_parameter[idx][1])**2), 2)
            
            result.append(euclidean)
            
        result_dict = {'Platinum' : result[0],
                       'Gold' : result[1],
                       'Silver' : result[2]}
        
        print(f"Hasil perhitungan Euclidean Distance dari user {username} adalah {result_dict}")
        
        for member, distance in result_dict.items():
            if distance == min(result):
                self.data[username] = member
                
                print(f"Membership yang sesuai untuk user {username} adalah: {member}")
    
    def calculate_price(self, username, list_harga):
        """
        Function to calculate the final price for user's spending after discounts based on membership.
        
        Parameters
        ----------
        username: string
            input username
        list_harga: list
            list of price for each spending
            
        Return
        ------
        final_price: float
            final price after discount
        """
        try:
            if username in self.data:
                membership = self.data.get(username)
                
                if membership == 'Platinum':
                    final_price = sum(list_harga) - (sum(list_harga) * 0.15)
                    
                    return final_price
                elif membership == 'Gold':
                    final_price = sum(list_harga) - (sum(list_harga) * 0.10)
                    
                    return final_price
                elif membership == 'Silver':
                    final_price = sum(list_harga) - (sum(list_harga) * 0.08)
                    
                    return final_price
                else:
                    raise Exception("Membership invalid")
            else:
                raise Exception("Username does not exist")
        except:
            raise Exception("Process Invalid")