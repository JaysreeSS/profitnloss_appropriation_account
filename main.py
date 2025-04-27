# Importing tabulate Module
from tabulate import tabulate

# Importing MySQL
import mysql.connector as ms
mycon = ms.connect (host='localhost', username='root', password='password')
mycursor = mycon.cursor()

code1 = 'create database project' # Creating a database
code2 = 'use project'
code3 = '''create table account(Dr_Particulars varchar(80) not null default "",
        Dr_Amount varchar(80) not null default "",
        Cr_Particulars varchar(80) not null default "",
        Cr_Amount varchar(80) not null default "")''' # Creating a Table

mycursor.execute(code1)
mycursor.execute(code2)
mycursor.execute(code3)

# Getting Basic Details
name_firm = input('Enter the Name of the Firm: ')
year = input('Enter when the Firm closes its Accounts each year: ')
no_partner = int(input('Enter the Number of Partners: '))
# Displaying Ratios
print('\nProfit/Loss Sharing Ratio:')
print('1. Equally')
print('2. In Ratio')
psr=int(input('Enter your choice (1 or 2): '))

# Setting Dictionaries
d_psr={} # Partner's Profit-Sharing Ratio
d_cap={} # Partner's Capital and Interest on Capital
d_draw={} # Partner's Drawings and Interest on Drawings
d_sal={} # Partner's Salary 
d_com={} # Partner's Commission
d_partner={} # Sum of Appropriations

# Getting Rate of Interest on Capital 
int_cap=int(input('\nEnter the rate of Interest on Capital p.a. (in %): '))

# Getting Rate of Interest on Drawings
d=input('\nDoes the partners have Drawings (y/n)? ')
if d=='y':
    int_draw=int(input('Enter the rate of Interest on Drawings (in %): '))

# Assigning Variables for FOR LOOP   
total_ratio=0 # Adding for Profit-Sharing Ratio
dr_int_cap=0 # Total Interest on Capital
dr_sal=0 # Total Salary 
dr_com=0 # Total Commission
cr_int_draw=0 # Total Interest on Drawings

for i in range(no_partner):
    print('\nEnter the Details of the Partner',i+1,':')
    name_partner = input('Enter the Name of the Partner: ')

    # Computing Partner's Profit Sharing Ratio
    if psr==2:
        ratio = int(input('Enter the Profit-Sharing Ratio of the Partner: '))
        total_ratio += ratio # Adding all Partner's Profit-Sharing Ratio
        d_psr[name_partner] = ratio # Uploading in Dict PSR

    # Computing Interest on Capital
    cap_con =int(input('Enter the amount of Capital contribution of the Partner: '))
    i_c = round(cap_con/100 * int_cap)
    dr_int_cap += i_c # Adding all Partner's Interest on Capital
    d_cap[name_partner] = [cap_con,i_c] # Uploading in Dict Capital
    
    # Computing Interest on Drawings
    if d=='y':
        draw =int(input('Enter the amount of Drawings of the Partner: '))
        i_d = round(draw/100 * int_draw)
        cr_int_draw += i_d # Adding all Partner's Interest on Drawings
        d_draw[name_partner] = [draw,i_d] # Uploading in Dict Drawings

    # Computing Salary
    sal=input('Does the Partner have Salary (y/n)? ')
    if sal=='y':
        amt_sal = int(input('Enter the amount of Salary p.a.: '))
        dr_sal += amt_sal # Adding all Partner's Salary
        d_sal[name_partner] = amt_sal # Uploading in Dict Salary

    if sal=='n':
        amt_sal=0

    # Computing Commission  
    com = input('Does the Partner have Commission (y/n)? ')
    if com=='y':
        amt_com = int(input('Enter the amount of Commission p.a.: '))
        dr_com += amt_com # Adding all Partner's Commission 
        d_com[name_partner] = amt_com # Uploading in Dict Commission

    if com=='n':
        amt_com=0
      
    ap_partner = i_c + amt_sal + amt_com  # Adding a Partner's Appropriations
    d_partner[name_partner] = ap_partner # Uploading in Dict Partner


# Preparing Profit and Loss Approriation Account
print('\nDoes the firm have:')
print('1. Earned Net Profit')
print('2. Incurred Net Loss')
net_pr_lo=int(input('Enter your choice (1 or 2): '))

# Earned Net Profit
if net_pr_lo==1:
    net_pr = int(input('Enter the amount of Net Profit: '))

    gr = round(net_pr/100 * 10) # General Reserve = 10% of Net Profit
    
    dr_ = dr_int_cap + dr_sal + dr_com + gr # Calculating Debit side
    cr_ = net_pr + cr_int_draw # Calculating Credit side

    if cr_ > dr_ :
        pr = cr_ - dr_

        # Inserting Values
        code4='''insert into account values ("To Interest on Capital A/c", '{0}',
        "By Profit and Loss A/c (Net Profit)", '{1}')'''. format(dr_int_cap, net_pr)
        mycursor.execute(code4)

        if dr_sal!=0 and dr_com==0 and cr_int_draw==0 :
            code5='''insert into account (Dr_Particulars,Dr_Amount)
            values ("To Salary A/c", '{0}')'''. format(dr_sal)
            mycursor.execute(code5)

        if dr_sal==0 and dr_com!=0 and cr_int_draw==0 :
            code6='''insert into account (Dr_Particulars,Dr_Amount)
            values ("By Commission A/c", '{0}')'''. format(dr_com)
            mycursor.execute(code6)

        if dr_sal==0 and dr_com==0 and cr_int_draw!=0 :
            code7='''insert into account (Cr_Particulars,Cr_Amount)
            values ("By Interest on Drawings A/c", '{0}')'''. format(cr_int_draw)
            mycursor.execute(code7)

        if dr_sal!=0 and dr_com!=0 and cr_int_draw==0 :
            code8='''insert into account (Dr_Particulars,Dr_Amount) values
            ("To Salary A/c", '{0}'), ("To Commission A/c", '{1}')'''. format(dr_sal, dr_com)
            mycursor.execute(code8)

        if dr_sal!=0 and dr_com==0 and cr_int_draw!=0 :
            code9='''insert into account values ("To Salary A/c", '{0}',
            "By Interest on Drawings A/c", '{1}' )'''. format(dr_sal, cr_int_draw)
            mycursor.execute(code9)

        if dr_sal==0 and dr_com!=0 and cr_int_draw!=0 :
            code10='''insert into account values ("To Commission A/c", '{0}',
            "By Interest on Drawings A/c", '{1}' )'''. format(dr_com, cr_int_draw)
            mycursor.execute(code10)

        if dr_sal!=0 and dr_com!=0 and cr_int_draw!=0 :
            code11='''insert into account values ("To Salary A/c", '{0}',
            "By Interest on Drawings A/c", '{1}' )'''. format(dr_sal, cr_int_draw)
            mycursor.execute(code11)

            code12='''insert into account( Dr_Particulars,Dr_Amount)
            values ("To Commission A/c", '{0}')'''. format(dr_com)
            mycursor.execute(code12)

        # Inserting General Reserve
        code13='''insert into account (Dr_Particulars,Dr_Amount)
        values ("To General Reserve A/c", '{0}')'''. format(gr)
        mycursor.execute(code13)

        # Inserting Distribution of Profits
        code14='''insert into account (Dr_Particulars)
        values ("To Profit transferred to Partners' Capital A/c")''' 
        mycursor.execute(code14)

        if psr==1:
            equally = round(pr/no_partner)
            
            for key1 in d_cap:
                code15='''insert into account (Dr_Particulars,Dr_Amount)
                values ('{0}', '{1}')'''. format(key1, equally)
                mycursor.execute(code15)

        if psr==2:

            for key2 in d_psr:
                res_ratio = round(pr/total_ratio * d_psr[key2])

                code16='''insert into account (Dr_Particulars,Dr_Amount)
                values ('{0}', '{1}')'''. format(key2, res_ratio)
                mycursor.execute(code16)

        # Inserting Total
        code17='''insert into account (Dr_Amount,Cr_Amount)
        values ('{0}', '{1}')'''. format('---------', '---------')
        mycursor.execute(code17)

        total = cr_

        code18='''insert into account (Dr_Amount,Cr_Amount)
        values ('{0}', '{1}')'''. format(total, total)
        mycursor.execute(code18)

        code19='''insert into account (Dr_Amount,Cr_Amount)
        values ('{0}', '{1}')'''. format('---------', '---------')
        mycursor.execute(code19)
        
        # Displaying the Table in Python
        mycursor.execute('select * from account')
        rows = mycursor.fetchall()

        print('\n\t\t\t\t\t\tBooks of {}'. format(name_firm) )
        print('\t\t\t\t\t     Profit and Loss Appropriation A/c')
        print('\t\t\t\t\t    for the year ended {}'. format(year) )
       
        print(tabulate(rows, headers=['Dr_Particulars','Dr_Amount',
                                          'Cr_Particulars','Cr_Amount'],
                       tablefmt='psql'))

        # Working Notes
        print('\nWorking Notes:-')
        
        print('-> Interest on Capital:')
        for k in d_cap:
            print('\t', k, '-Rs.', d_cap[k][1])

        if dr_sal!=0 :
            print('-> Salary:')
            for l in d_sal:
                print('\t', l, '-Rs.', d_sal[l])

        if dr_com!=0 :
            print('-> Commission:')
            for m in d_com:
                print('\t', m, '-Rs.', d_com[m])

        if cr_int_draw!=0:
            print('-> Interest on Drawings:')
            for n in d_draw:
                print('\t', n, '-Rs.', d_draw[n][1])

        print('------------------------------')

        ch=input('\nDo you want to make any changes in General Reserve (y/n)? ')
        if ch=='y':
            m=input('\nDo you want to maintain General Reserve (y/n)? ')

            #Updating General Reserve
            if m=='y':                
                u=int(input('\nEnter the amount to be updated: '))
                code20='''update account set Dr_Amount='{0}'
                where Dr_Particulars = "To General Reserve A/c" '''. format(u)
                mycursor.execute(code20)

                dr_ = dr_int_cap + dr_sal + dr_com + u # Calculating Debit side
                cr_ = net_pr + cr_int_draw # Calculating Credit side

                pr = cr_ - dr_

                if psr==1:
                    equally = round(pr/no_partner)
                    
                    for key1 in d_cap:
                        code21='''update account set Dr_Amount='{0}'
                        where Dr_Particulars = '{1}' '''. format(equally, key1)
                        mycursor.execute(code21)

                if psr==2:

                    for key2 in d_psr:
                        res_ratio = round(pr/total_ratio * d_psr[key2])

                        code22='''update account set Dr_Amount='{0}'
                        where Dr_Particulars = '{1}' '''. format(res_ratio, key2)
                        mycursor.execute(code22)

                print('\nUpdated successfully')
                
                # Displaying the Table in Python
                mycursor.execute('select * from account')
                rows = mycursor.fetchall()

                print('\n\t\t\t\t\t\tBooks of {}'. format(name_firm) )
                print('\t\t\t\t\t     Profit and Loss Appropriation A/c')
                print('\t\t\t\t\t    for the year ended {}'. format(year) )
               
                print(tabulate(rows, headers=['Dr_Particulars','Dr_Amount',
                                                  'Cr_Particulars','Cr_Amount'],
                               tablefmt='psql'))

                # Working Notes
                print('\nWorking Notes:-')
                
                print('-> Interest on Capital:')
                for k in d_cap:
                    print('\t', k, '-Rs.', d_cap[k][1])

                if dr_sal!=0 :
                    print('-> Salary:')
                    for l in d_sal:
                        print('\t', l, '-Rs.', d_sal[l])

                if dr_com!=0 :
                    print('-> Commission:')
                    for m in d_com:
                        print('\t', m, '-Rs.', d_com[m])

                if cr_int_draw!=0:
                    print('-> Interest on Drawings:')
                    for n in d_draw:
                        print('\t', n, '-Rs.', d_draw[n][1])

                print('------------------------------')

            #Deleting General Reserve
            if m=='n':
                code23='''delete from account where
                Dr_Particulars = "To General Reserve A/c" '''
                mycursor.execute(code23)

                dr_ = dr_int_cap + dr_sal + dr_com # Calculating Debit side
                cr_ = net_pr + cr_int_draw # Calculating Credit side

                pr = cr_ - dr_

                if psr==1:
                    equally = round(pr/no_partner)
                    
                    for key1 in d_cap:
                        code24='''update account set Dr_Amount='{0}'
                        where Dr_Particulars = '{1}' '''. format(equally, key1)
                        mycursor.execute(code24)

                if psr==2:

                    for key2 in d_psr:
                        res_ratio = round(pr/total_ratio * d_psr[key2])

                        code25='''update account set Dr_Amount='{0}'
                        where Dr_Particulars = '{1}' '''. format(res_ratio, key2)
                        mycursor.execute(code25)

                print('\nDeleted successfully')
                
                # Displaying the Table in Python
                mycursor.execute('select * from account')
                rows = mycursor.fetchall()

                print('\n\t\t\t\t\t\tBooks of {}'. format(name_firm) )
                print('\t\t\t\t\t     Profit and Loss Appropriation A/c')
                print('\t\t\t\t\t    for the year ended {}'. format(year) )
               
                print(tabulate(rows, headers=['Dr_Particulars','Dr_Amount',
                                                  'Cr_Particulars','Cr_Amount'],
                               tablefmt='psql'))

                # Working Notes
                print('\nWorking Notes:-')
                
                print('-> Interest on Capital:')
                for k in d_cap:
                    print('\t', k, '-Rs.', d_cap[k][1])

                if dr_sal!=0 :
                    print('-> Salary:')
                    for l in d_sal:
                        print('\t', l, '-Rs.', d_sal[l])

                if dr_com!=0 :
                    print('-> Commission:')
                    for m in d_com:
                        print('\t', m, '-Rs.', d_com[m])

                if cr_int_draw!=0:
                    print('-> Interest on Drawings:')
                    for n in d_draw:
                        print('\t', n, '-Rs.', d_draw[n][1])

                print('------------------------------')


        if ch=='n':
            print('------------------------------------------------------------')
        
# Incured loss
if net_pr_lo==2:
    net_lo=int(input('Enter the amount of Net Loss: '))
    dr_ = net_lo
    cr_ = cr_int_draw
    lo = dr_ - cr_
    
    # Inserting Values
    if cr_int_draw!=0 :
            code26='''insert into account values ("To Profit and Loss A/c (Net Loss)", '{0}',
            "By Interest on Drawings A/c", '{1}')'''. format(net_lo, cr_int_draw)
            mycursor.execute(code26)

    if cr_int_draw==0 :
        code27='''insert into account (Dr_Particulars,Dr_Amount)
        values ("To Profit and Loss A/c (Net Loss)", '{0}')'''. format(net_lo)
        mycursor.execute(code27)

    # Inserting Distribution of Loss
    code28='''insert into account (Cr_Particulars)
    values ("By Loss transferred to Partners' Capital A/c")''' 
    mycursor.execute(code28)
           
    if psr==1:
        equally = round(lo/no_partner)

        for key1 in d_cap:
            code29='''insert into account (Cr_Particulars,Cr_Amount)
            values ('{0}','{1}')'''. format(key1, equally)
            mycursor.execute(code29)

    if psr==2:
        
        for key2 in d_psr:
            res_ratio = round(lo/total_ratio * d_psr[key2] )

            code30='''insert into account(Cr_Particulars,Cr_Amount)
            values ('{0}','{1}')'''. format(key2, res_ratio)
            mycursor.execute(code30)

    # Inserting Total
    code31='''insert into account (Dr_Amount,Cr_Amount)
    values ('{0}', '{1}')'''. format('---------', '---------')
    mycursor.execute(code31)

    total = dr_

    code32='''insert into account (Dr_Amount,Cr_Amount)
    values ('{0}', '{1}')'''. format(total, total)
    mycursor.execute(code32)

    code33='''insert into account (Dr_Amount,Cr_Amount)
    values ('{0}', '{1}')'''. format('---------', '---------')
    mycursor.execute(code33)

    # Displaying the Table in Python
    mycursor.execute('select * from account')
    rows = mycursor.fetchall()

    print('\n\t\t\t\t\t\tBooks of {}'. format(name_firm) )
    print('\t\t\t\t\t     Profit and Loss Appropriation A/c')
    print('\t\t\t\t\t    for the year ended {}'. format(year) )
       
    print(tabulate(rows, headers=['Dr_Particulars','Dr_Amount',
                                      'Cr_Particulars','Cr_Amount'],
                   tablefmt='psql'))

    # Working Notes
    if cr_int_draw!=0:
        print('\nWorking Notes:-')
     
        print('-> Interest on Drawings:')
        for n in d_draw:
            print('\t', n, '-Rs.', d_draw[n][1])

        print('------------------------------')
              
mycon.commit()

mycursor.execute('drop database project')

mycon.close()
