from nba import *
from pymongo import MongoClient
from requests_html import HTMLSession,AsyncHTMLSession

client = MongoClient("mongodb+srv://shawntez32:Tezzyk32@cluster0.wpzbm.mongodb.net/?retryWrites=true&w=majority")

nba_database = client["nbaDatabase"]
Date = ''

    
nba_2023_stats = []
global index1
index1 = 0

async def nbadb(nba_team,year):
    sample_list = []
    a = 0
    content = ('https://www.basketball-reference.com/teams/{}/{}/gamelog/'.format(nba_team,year))
    session = HTMLSession()
    r = await session.get(content)
    r.html.render(sleep=2,keep_page=True,scrolldown=3)
    name = "{}_{}".format(nba_team,year)
    td = r.html.find('td')
    for td1 in td:
        sample_list.append(td1.text)
        Rk = sample_list[0::40]
        Date = sample_list[1::40]
        Home = sample_list[2::40]
        Opp = sample_list[3::40]
        WL = sample_list[4::40]
        Tm = sample_list[5::40]
        Opp2 = sample_list[6::40]
        FG = sample_list[7::40]
        FGA = sample_list[8::40]
        FGp = sample_list[9::40]
        P3 = sample_list[10::40]
        PA3 = sample_list[11::40]
        Pp3 = sample_list[12::40]
        FT = sample_list[13::40]
        FTA = sample_list[14::40]
        FTp = sample_list[15::40]
        ORB = sample_list[16::40]
        TRB = sample_list[17::40]
        AST = sample_list[18::40]
        STL = sample_list[19::40]
        BLK = sample_list[20::40]
        TOV = sample_list[21::40]
        PF = sample_list[22::40]
        Missing = sample_list[23::40]
        OFG = sample_list[24::40]
        OFGA = sample_list[25::40]
        OFGp = sample_list[26::40]
        OP3 = sample_list[27::40]
        OPA3 = sample_list[28::40]
        OPp3 = sample_list[29::40]
        OFT = sample_list[30::40]
        OFTA= sample_list[31::40]
        OFTp = sample_list[32::40]
        OORB = sample_list[33::40]
        OTRB = sample_list[34::40]
        OAST = sample_list[35::40]
        OSTL = sample_list[36::40]
        OBLK = sample_list[37::40]
        OTOV = sample_list[38::40]
        P = sample_list[39::40]
        Stats = {'Rk':Rk,'Date':Date,'Home':Home,'W/L':WL,'Opp':Opp,'Tm':Tm,'Opp2':Opp2,'FG':FG,'FGA':FGA,'FG%':FGp,'3P':P3,'3PA':PA3,'3P%':Pp3,'FT':FT,'FTA':FTA,'FT%':FTp,'ORB':ORB,'TRB':TRB,'AST':AST,'STL':STL,'BLK':BLK,'TOV':TOV,'PF':PF,'OFG':OFG,'OFGA':OFGA,'OFG%':OFGp,'O3P':OP3,'3PA':OPA3,'O3P%':OPp3,'OFT':OFT,'OFTA':OFTA,'OFT%':OFTp,'OORB':OORB,'OTRB':OTRB,'OAST':OAST,'OSTL':OSTL,'OBLK':OBLK,'OTOV':OTOV,'P':P}
    for e in Rk:
        rks = Rk[a]
        dates = Date[a]
        homes = Home[a]
        opps = Opp[a]
        wls = WL[a]
        tms = Tm[a]
        opp2s = Opp2[a]
        fgs = FG[a]
        fgas = FGA[a]
        fgps = FGp[a]
        p3s = P3[a]
        pa3s = PA3[a]
        pp3s = Pp3[a]
        fts = FT[a]
        ftas = FTA[a]
        ftps = FTp[a]
        orbs = ORB[a]
        trbs = TRB[a]
        asts = AST[a]
        stls = STL[a]
        blks = BLK[a]
        tovs = TOV[a]
        pfs = PF[a]
        mssing = Missing[a]
        ofgs = OFG[a]
        ofgas = OFGA[a]
        ofgps = OFGp[a]
        op3s = OP3[a]
        opa3s = OPA3[a]
        opp3s = OPp3[a]
        ofts = OFT[a]
        oftas= OFTA[a]
        oftps = OFTp[a]
        oorbs = OORB[a]
        otrbs = OTRB[a]
        oasts = OAST[a]
        ostls = OSTL[a]
        oblks = OBLK[a]
        otovs = OTOV[a]
        ps = P[a]
        Stats2 = {'Rk':rks,'Date':dates,'Home':homes,'W/L':wls,'Opp':opps,'Tm':tms,'Opp2':opp2s,'FG':fgs,'FGA':fgas,'FG%':fgps,'3P':p3s,'3PA':pa3s,'3P%':pp3s,'FT':fts,'FTA':ftas,'FT%':ftps,'ORB':orbs,'TRB':trbs,'AST':asts,'STL':stls,'BLK':blks,'TOV':tovs,'PF':pfs,'OFG':ofgs,'OFGA':ofgas,'OFG%':ofgps,'O3P':op3s,'3PA':opa3s,'O3P%':opp3s,'OFT':ofts,'OFTA':oftas,'OFT%':oftps,'OORB':oorbs,'OTRB':otrbs,'OAST':oasts,'OSTL':ostls,'OBLK':oblks,'OTOV':otovs,'P':ps}
        try:
            rec = nba_database.create_collection(name='{}'.format(name))
        except:
            rec = nba_database["{}".format(name)]
        rec.insert_one(Stats2)
        a += 1

def nba_get_stats(nba_team,year):
    sample_list = []
    global index1
    a = 0
    content = ('https://www.basketball-reference.com/teams/{}/{}/gamelog/'.format(nba_team,year))
    session = HTMLSession()
    r = session.get(content)
    r.html.render(sleep=4,keep_page=True,scrolldown=3)
    name = "{}_{}".format(nba_team,year)
    td = r.html.find('td')
    for td1 in td:
        sample_list.append(td1.text)
        Rk = sample_list[0::40]
        Date = sample_list[1::40]
        Home = sample_list[2::40]
        Opp = sample_list[3::40]
        WL = sample_list[4::40]
        Tm = sample_list[5::40]
        Opp2 = sample_list[6::40]
        FG = sample_list[7::40]
        FGA = sample_list[8::40]
        FGp = sample_list[9::40]
        P3 = sample_list[10::40]
        PA3 = sample_list[11::40]
        Pp3 = sample_list[12::40]
        FT = sample_list[13::40]
        FTA = sample_list[14::40]
        FTp = sample_list[15::40]
        ORB = sample_list[16::40]
        TRB = sample_list[17::40]
        AST = sample_list[18::40]
        STL = sample_list[19::40]
        BLK = sample_list[20::40]
        TOV = sample_list[21::40]
        PF = sample_list[22::40]
        Missing = sample_list[23::40]
        OFG = sample_list[24::40]
        OFGA = sample_list[25::40]
        OFGp = sample_list[26::40]
        OP3 = sample_list[27::40]
        OPA3 = sample_list[28::40]
        OPp3 = sample_list[29::40]
        OFT = sample_list[30::40]
        OFTA= sample_list[31::40]
        OFTp = sample_list[32::40]
        OORB = sample_list[33::40]
        OTRB = sample_list[34::40]
        OAST = sample_list[35::40]
        OSTL = sample_list[36::40]
        OBLK = sample_list[37::40]
        OTOV = sample_list[38::40]
        P = sample_list[39::40]
        Stats = {'Rk':Rk,'Date':Date,'Home':Home,'W/L':WL,'Opp':Opp,'Tm':Tm,'Opp2':Opp2,'FG':FG,'FGA':FGA,'FG%':FGp,'3P':P3,'3PA':PA3,'3P%':Pp3,'FT':FT,'FTA':FTA,'FT%':FTp,'ORB':ORB,'TRB':TRB,'AST':AST,'STL':STL,'BLK':BLK,'TOV':TOV,'PF':PF,'OFG':OFG,'OFGA':OFGA,'OFG%':OFGp,'O3P':OP3,'3PA':OPA3,'O3P%':OPp3,'OFT':OFT,'OFTA':OFTA,'OFT%':OFTp,'OORB':OORB,'OTRB':OTRB,'OAST':OAST,'OSTL':OSTL,'OBLK':OBLK,'OTOV':OTOV,'P':P}
        e = {"Team":nba_team,"Stats":Stats,"index":index1}
        nba_2023_stats.append(e)
    index1 += 1

years = [2022]
e = 0

for team in nba_dicts:
   for year in years:
    if e < 8:
        data = nba_get_stats(team['abv'],year)
e += 1