import datetime as DT
import io
import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = 'warn'

content = '''     ssno        lname         fname    pos_title             ser  gender  dob 
0    23456789    PLILEY     JODY        BUDG ANAL             0560  F      031871 
1    987654321   NOEL       HEATHER     PRTG SRVCS SPECLST    1654  F      120852
2    234567891   SONJU      LAURIE      SUPVY CONTR SPECLST   1102  F      010999
3    345678912   MANNING    CYNTHIA     SOC SCNTST            0101  F      081692
4    456789123   NAUERTZ    ELIZABETH   OFF AUTOMATION ASST   0326  F      031387'''

df = pd.read_csv(io.StringIO(content), sep='\s{2,}')
df['dob'] = df['dob'].apply('{:06}'.format)

now = pd.Timestamp('now')
df['dob'] = pd.to_datetime(df['dob'], format='%m%d%y')    # 1
df['dob'] = df['dob'].where(df['dob'] < now, df['dob'] -  np.timedelta64(100, 'Y'))   # 2
df['age'] = (now - df['dob']).astype('<m8[Y]')    # 3
print(df)