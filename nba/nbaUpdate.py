import datetime as dt
from pymongo import MongoClient
from requests_html import HTMLSession

now = dt.datetime.now()
today = dt.date(now.year,now.month,now.day)
current_year = now.year

season_start = dt.date(2022,10,19)
season_end = ''
playoff_start = ''
playoff_end = ''

last_updated = ''

client = MongoClient("mongodb+srv://shawntez32:Tezzyk32@cluster0.wpzbm.mongodb.net/?retryWrites=true&w=majority")

nba_database = client["nbaDatabase"]

new_game_played = False

def checkGames(team,lastUpdated):
    if last_updated == today:
        pass
    else:
        year = current_year
        content = ('https://www.basketball-reference.com/teams/{}/{}/gamelog/'.format(team,year))
        session = HTMLSession()
        r = session.get(content)
        r.html.render(sleep=4,keep_page=True,scrolldown=3)
        name = "{}_{}".format(team,year)
        rec = nba_database["{}".format(name)]
        db_len = 0
        for x in rec.find():
            db_len += 1
        td = r.html.find('td')
        stat_len = len(td) / 40
        if stat_len > db_len:
            updateGameStats(team)
        else:
            pass


def updateGameStats(team):
    sample_list = []
    a = 0
    content = ('https://www.basketball-reference.com/teams/{}/{}/gamelog/'.format(team,current_year))
    session = HTMLSession()
    r = session.get(content)
    r.html.render(sleep=4,keep_page=True,scrolldown=3)
    name = "{}_{}".format(team,current_year)
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
        rks = Rk[-1]
        dates = Date[-1]
        homes = Home[-1]
        opps = Opp[-1]
        wls = WL[-1]
        tms = Tm[-1]
        opp2s = Opp2[-1]
        fgs = FG[-1]
        fgas = FGA[-1]
        fgps = FGp[-1]
        p3s = P3[-1]
        pa3s = PA3[-1]
        pp3s = Pp3[-1]
        fts = FT[-1]
        ftas = FTA[-1]
        ftps = FTp[-1]
        orbs = ORB[-1]
        trbs = TRB[-1]
        asts = AST[-1]
        stls = STL[-1]
        blks = BLK[-1]
        tovs = TOV[-1]
        pfs = PF[-1]
        mssing = Missing[-1]
        ofgs = OFG[-1]
        ofgas = OFGA[-1]
        ofgps = OFGp[-1]
        op3s = OP3[-1]
        opa3s = OPA3[-1]
        opp3s = OPp3[-1]
        ofts = OFT[-1]
        oftas= OFTA[-1]
        oftps = OFTp[-1]
        oorbs = OORB[-1]
        otrbs = OTRB[-1]
        oasts = OAST[-1]
        ostls = OSTL[-1]
        oblks = OBLK[-1]
        otovs = OTOV[-1]
        ps = P[-1]
        Stats2 = {'Rk':rks,'Date':dates,'Home':homes,'W/L':wls,'Opp':opps,'Tm':tms,'Opp2':opp2s,'FG':fgs,'FGA':fgas,'FG%':fgps,'3P':p3s,'3PA':pa3s,'3P%':pp3s,'FT':fts,'FTA':ftas,'FT%':ftps,'ORB':orbs,'TRB':trbs,'AST':asts,'STL':stls,'BLK':blks,'TOV':tovs,'PF':pfs,'OFG':ofgs,'OFGA':ofgas,'OFG%':ofgps,'O3P':op3s,'3PA':opa3s,'O3P%':opp3s,'OFT':ofts,'OFTA':oftas,'OFT%':oftps,'OORB':oorbs,'OTRB':otrbs,'OAST':oasts,'OSTL':ostls,'OBLK':oblks,'OTOV':otovs,'P':ps}
        try:
            rec = nba_database.create_collection(name='{}'.format(name))
        except:
            rec = nba_database["{}".format(name)]
        rec.insert_one(Stats2)
        a += 1

