import datetime as dt
import sqlite3
import pandas as pd
from nba import nba_dicts

now = dt.datetime.now()
today = dt.date(now.year,now.month,now.day)

class NbaTeam():
    w = 0
    l = 0

    def __init__(self,Rk=1,Abr='ATL',Name="Seattle Sonics",Home=False,Date=today,Opp=0,WL=0,Tm=107.3,Opp2=105.5,FG=46,FGA=104,FGP=46/104,PM3=8,PA3=22,P3P=8/22,FT=17,FTA=25,FTP=17/25,ORB=14,TRB=36,AST=19,STL=11,BLK=11,TOV=11,PF=17,OFG=41,OFGA=96,OFGP=41/96,OP3=7,OPA3=15,OP3P=7/15,OFT=20,OFTA=24,OFTP=20/24,OORB=14,OTRB=31,OAST=16,OSTL=9,OBLK=13,OTOV=16,P=19):
        self.rk = Rk
        self.abr = Abr
        self.name = Name
        self.date = Date
        self.home = Home
        self.opp = Opp
        self.wl = WL
        self.tm = Tm
        self.opp2 = Opp2
        self.fg = FG
        self.fga = FGA
        self.fgp = FGP
        self.p3 = PM3
        self.pa3 = PA3
        self.pp3 = P3P
        self.ft = FT
        self.fta = FTA
        self.ftp = FTP
        self.orb = ORB
        self.trb = TRB
        self.ast = AST
        self.stl = STL
        self.blk = BLK
        self.tov = TOV
        self.pf = PF
        self.ofg = OFG
        self.ofga = OFGA
        self.ofgp = OFGP
        self.op3 = OP3
        self.opa3 = OPA3
        self.opp3 = OP3P
        self.oft = OFT
        self.ofta= OFTA
        self.oftp = OFTP
        self.oorb = OORB
        self.otrb = OTRB
        self.oast = OAST
        self.ostl = OSTL
        self.oblk = OBLK
        self.otov = OTOV
        self.p = P


    def get_stats(self,team,year):
        self.w = 0
        self.l = 0
        team = team
        year = year
        db_path = sqlite3.connect(f'{team}-{year}-stats.db')
        conn = db_path
        cur = conn.cursor()
        cur.execute('SELECT * FROM Statz')
        row = cur.fetchall()
        team_stats = pd.DataFrame(row, columns=['Rk','Date','Home','WL','Opp','Tm','Opp2','FG','FGA','FGP','T3P','PA3','PP3','FT','FTA','FTP','ORB','TRB','AST','STL','BLK','TOV','PF','OFG','OFGA','OFGP','OP3','OPA3','OPP3','OFT','OFTA','OFTP','OORB','OTRB','OAST','OSTL','OBLK','OTOV','P'])
        date = team_stats['Date']
        self.tm = sum(team_stats['Tm'].astype(int)) / len(team_stats['Tm'])
        self.opp2 = team_stats['Opp2']
        self.home = team_stats['Home']
        self.wl = team_stats['WL']
        self.opp = team_stats['Opp']
        self.fg = sum(team_stats['FG'].astype(int)) / len(team_stats['FG'])
        self.fga = sum(team_stats['FGA'].astype(int)) / len(team_stats['FGA'])
        self.fgp = sum(team_stats['FG'].astype(int)) / sum(team_stats['FGA'].astype(int))
        self.p3 = sum(team_stats['T3P'].astype(int)) / len(team_stats['T3P'])
        self.pa3 = sum(team_stats['PA3'].astype(int)) / len(team_stats['PA3'])
        self.pp3 = sum(team_stats['T3P'].astype(int)) / sum(team_stats['PA3'].astype(int))
        self.ft = sum(team_stats['FT'].astype(int)) / len(team_stats['FT'])
        self.fta = sum(team_stats['FTA'].astype(int)) / len(team_stats['FTA'])
        self.ftp = sum(team_stats['FT'].astype(int)) / sum(team_stats['FTA'].astype(int))
        self.orb =sum(team_stats['ORB'].astype(int)) / len(team_stats['ORB'])
        self.trb = sum(team_stats['AST'].astype(int)) / len(team_stats['AST'])
        self.stl = sum(team_stats['STL'].astype(int)) / len(team_stats['STL'])
        self.blk = sum(team_stats['BLK'].astype(int)) / len(team_stats['BLK'])
        self.tov = sum(team_stats['TOV'].astype(int)) / len(team_stats['TOV'])
        self.pf = sum(team_stats['PF'].astype(int)) / len(team_stats['TOV'])
        self.ofg = sum(team_stats['OFG'].astype(int)) / len(team_stats['TOV'])
        self.ofga = sum(team_stats['OFGA'].astype(int)) / len(team_stats['TOV'])
        self.ofgp = sum(team_stats['OFG'].astype(int)) / sum(team_stats['OFGA'].astype(int))
        self.op3 = sum(team_stats['OP3'].astype(int)) / len(team_stats['OP3'])
        self.op3a = sum(team_stats['OPA3'].astype(int)) / len(team_stats['OP3'])
        self.opp3 = sum(team_stats['OP3'].astype(int)) / sum(team_stats['OPA3'].astype(int))
        self.oft = sum(team_stats['OFT'].astype(int)) / len(team_stats['OFT'])
        self.ofta = sum(team_stats['OFTA'].astype(int)) / len(team_stats['OFT'])
        self.oftp = sum(team_stats['OFT'].astype(int)) / sum(team_stats['OFTA'].astype(int))
        self.oorb = sum(team_stats['OORB'].astype(int)) / len(team_stats['OORB'])
        self.otrb = sum(team_stats['OTRB'].astype(int)) / len(team_stats['OORB'])
        self.oast = sum(team_stats['OAST'].astype(int)) / len(team_stats['OORB'])
        self.ostl = sum(team_stats['OSTL'].astype(int)) / len(team_stats['OORB'])
        self.oblk = sum(team_stats['OBLK'].astype(int)) / len(team_stats['OORB'])
        self.otov = sum(team_stats['OTOV'].astype(int)) / len(team_stats['OORB'])
        self.p = sum(team_stats['P'].astype(int)) / len(team_stats['OORB'])
        for e in self.wl:
            if e == 'W':
                self.w += 1
            else:
                self.l += 1
            self.wl = f'{self.w}-{self.l}'

    def last5(self,team,year):
        self.w = 0
        self.l = 0
        team = self.abr
        year = year
        conn = sqlite3.connect(f'{team}-{year}-stats.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Statz')
        row = cur.fetchall()
        team_stats = pd.DataFrame(row, columns=['Rk','Date','Home','WL','Opp','Tm','Opp2','FG','FGA','FGP','T3P','PA3','PP3','FT','FTA','FTP','ORB','TRB','AST','STL','BLK','TOV','PF','OFG','OFGA','OFGP','OP3','OPA3','OPP3','OFT','OFTA','OFTP','OORB','OTRB','OAST','OSTL','OBLK','OTOV','P'])
        date = team_stats['Date']
        self.tm = sum(team_stats['Tm'].tail(5).astype(int)) / 5
        self.opp2 = team_stats['Opp2'].tail(5)
        self.home = team_stats['Home'].tail(5)
        self.wl = team_stats['WL'].tail(5)
        self.opp = team_stats['Opp'].tail(5)
        self.fg = sum(team_stats['FG'].tail(5).astype(int)) / 5
        self.fga = sum(team_stats['FGA'].tail(5).astype(int)) / 5
        self.fgp = sum(team_stats['FG'].tail(5).astype(int)) / sum(team_stats['FGA'].tail(5).astype(int))
        self.p3 = sum(team_stats['T3P'].tail(5).astype(int)) / 5
        self.pa3 = sum(team_stats['PA3'].tail(5).astype(int)) / 5
        self.pp3 = sum(team_stats['T3P'].tail(5).astype(int)) / sum(team_stats['PA3'].tail(5).astype(int))
        self.ft = sum(team_stats['FT'].tail(5).astype(int)) / 5
        self.fta = sum(team_stats['FTA'].tail(5).astype(int)) / 5
        self.ftp = sum(team_stats['FT'].tail(5).astype(int)) / sum(team_stats['FTA'].tail(5).astype(int))
        self.orb =sum(team_stats['ORB'].tail(5).astype(int)) / 5
        self.trb = sum(team_stats['AST'].tail(5).astype(int)) / 5
        self.stl = sum(team_stats['STL'].tail(5).astype(int)) / 5
        self.blk = sum(team_stats['BLK'].tail(5).astype(int)) / 5
        self.tov = sum(team_stats['TOV'].tail(5).astype(int)) / 5
        self.pf = sum(team_stats['PF'].tail(5).astype(int)) / 5
        self.ofg = sum(team_stats['OFG'].tail(5).astype(int)) / 5
        self.ofga = sum(team_stats['OFGA'].tail(5).astype(int)) / 5
        self.ofgp = sum(team_stats['OFG'].tail(5).astype(int)) / sum(team_stats['OFGA'].tail(5).astype(int))
        self.op3 = sum(team_stats['OP3'].tail(5).astype(int)) / 5
        self.op3a = sum(team_stats['OPA3'].tail(5).astype(int)) / 5
        self.opp3 = sum(team_stats['OP3'].tail(5).astype(int)) / sum(team_stats['OPA3'].tail(5).astype(int))
        self.oft = sum(team_stats['OFT'].tail(5).astype(int)) / 5
        self.ofta = sum(team_stats['OFTA'].tail(5).astype(int)) / 5
        self.oftp = sum(team_stats['OFT'].tail(5).astype(int)) / sum(team_stats['OFTA'].tail(5).astype(int))
        self.oorb = sum(team_stats['OORB'].tail(5).astype(int)) / 5
        self.otrb = sum(team_stats['OTRB'].tail(5).astype(int)) / 5
        self.oast = sum(team_stats['OAST'].tail(5).astype(int)) / 5
        self.ostl = sum(team_stats['OSTL'].tail(5).astype(int)) / 5
        self.oblk = sum(team_stats['OBLK'].tail(5).astype(int)) / 5
        self.otov = sum(team_stats['OTOV'].tail(5).astype(int)) / 5
        self.p = sum(team_stats['P'].tail(5).astype(int)) / 5
        for e in self.wl:
            if e == 'W':
                self.w += 1
                self.wl = f'{self.w}-{self.l}'
            else:
                self.l += 1
                self.wl = f'{self.w}-{self.l}'

print(nba_dicts)