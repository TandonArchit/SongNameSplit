

#####################################################################

## Testing function
def test(dic1, dic2):
    
    if not dic1 or not dic2:
        print("Test FAILED | ", dic1, " =/= ", dic2)
        return False

    elif dic1 != dic2:
        print("Test FAILED | ", dic1, " =/= ", dic2)
        return False
    
    elif dic1 == dic2:
        print("Test Passed")
        return True

    else:
        print("Unusual Case")
        return False


#####################################################################
#####################################################################

def runTests():

    import time
    import SongNameSplit

    count = 0
    totaltests = 125

    startTime = time.perf_counter()

    try:
      if test(SongNameSplit.namesplit("Alan Walker, Sabrina Carpenter & Farruko - On My Way"), {'artist': 'Alan Walker, Sabrina Carpenter & Farruko', 'songname': 'On My Way'}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Charlie Puth - We Don't Talk Anymore (feat. Selena Gomez) [Official Video]"), {'artist': 'Charlie Puth', 'songname': "We Don't Talk Anymore"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Alec Benjamin - Let Me Down Slowly [Official Music Video]"), {'artist': 'Alec Benjamin', 'songname': "Let Me Down Slowly"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Trevor Daniel - Falling (Official Music Video)"), {'artist': 'Trevor Daniel', 'songname': "Falling"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Sub Urban - Cradles [Official Music Video]"), {'artist': 'Sub Urban', 'songname': "Cradles"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("The Chainsmokers - Closer (Lyrics) ft. Halsey"), {'artist': 'The Chainsmokers', 'songname': "Closer"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Justin Bieber - Sorry (Lyrics)"), {'artist': 'Justin Bieber', 'songname': "Sorry"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Clean Bandit - Rockabye (Lyrics) Ft. Sean Paul & Anne-Marie"), {'artist': 'Clean Bandit', 'songname': "Rockabye"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Sia - Unstoppable (Lyrics)"), {'artist': 'Sia', 'songname': "Unstoppable"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Sia - Cheap Thrills (Lyric Video) ft. Sean Paul"), {'artist': 'Sia', 'songname': "Cheap Thrills"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Mercy - Badshah Feat. Lauren Gottlieb | Official Music Video | Latest Hit Song 2017"), {'artist': 'Badshah', 'songname': "Mercy"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Imran Khan - Amplifier (Official Music Video)"), {'artist': 'Imran Khan', 'songname': "Amplifier"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Alok & Alan Walker - Headlights (feat. KIDDO) [Official Lyric Video]"), {'artist': 'Alok & Alan Walker', 'songname': "Headlights"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("TLC - No Scrubs (Official Video)"), {'artist': 'TLC', 'songname': "No Scrubs"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("J Balvin, Willy William - Mi Gente (Official Video)"), {'artist': 'J Balvin, Willy William', 'songname': "Mi Gente"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("The Weeknd - Blinding Lights (Official Video)"), {'artist': 'The Weeknd', 'songname': "Blinding Lights"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Celina Sharma, Emiway Bantai - Lean On (Official Video)"), {'artist': 'Celina Sharma, Emiway Bantai', 'songname': "Lean On"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Marc Wavy - Daydreaming (Official Lyric Video)"), {'artist': 'Marc Wavy', 'songname': "Daydreaming"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("DHARIA - Sugar & Brownies (by Monoir) [Official Video]"), {'artist': 'DHARIA', 'songname': "Sugar & Brownies"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Daddy Yankee & Snow - Con Calma (Official Video)"), {'artist': 'Daddy Yankee & Snow', 'songname': "Con Calma"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Still Woozy - Goodie Bag"), {'artist': 'Still Woozy', 'songname': "Goodie Bag"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Ed Sheeran - South of the Border (feat. Camila Cabello & Cardi B) [Official Music Video]"), {'artist': 'Ed Sheeran', 'songname': "South of the Border"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Trevor Daniel, Selena Gomez - Past Life (Official Video)"), {'artist': 'Trevor Daniel, Selena Gomez', 'songname': "Past Life"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("ElyOtto - SugarCrash! (Official Video)"), {'artist': 'ElyOtto', 'songname': "SugarCrash!"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Deep Chills - Run Free (feat. IVIE) (Official Audio) TikTok #shoechange"), {'artist': 'Deep Chills', 'songname': "Run Free"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Kesha - Cannibal (Official Lyric Video)"), {'artist': 'Kesha', 'songname': "Cannibal"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Ke$ha - TiK ToK (Official HD Video)"), {'artist': 'Ke$ha', 'songname': "TiK ToK"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("MEDUZA, Becky Hill, Goodboys - Lose Control (Official Video)"), {'artist': 'MEDUZA, Becky Hill, Goodboys', 'songname': "Lose Control"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("TONES AND I - DANCE MONKEY (OFFICIAL VIDEO)"), {'artist': 'TONES AND I', 'songname': "DANCE MONKEY"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Dua Lipa - Don't Start Now (Official Music Video)"), {'artist': 'Dua Lipa', 'songname': "Don't Start Now"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("salem ilese – mad at disney (official music video)"), {'artist': 'salem ilese', 'songname': "mad at disney"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Billie Eilish - Therefore I Am (Official Music Video)"), {'artist': 'Billie Eilish', 'songname': "Therefore I Am"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Dua Lipa - Levitating Featuring DaBaby (Official Music Video)"), {'artist': 'Dua Lipa', 'songname': "Levitating"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Serena - Safari (Official Video)"), {'artist': 'Serena', 'songname': "Safari"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Alan Walker & Ava Max - Alone, Pt. II"), {'artist': 'Alan Walker & Ava Max', 'songname': "Alone, Pt. II"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Jennifer Lopez - On The Floor ft. Pitbull"), {'artist': 'Jennifer Lopez', 'songname': "On The Floor"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Meghan Trainor - Me Too"), {'artist': 'Meghan Trainor', 'songname': "Me Too"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Alesso x CORSAK - Going Dumb (Official Audio)"), {'artist': 'Alesso x CORSAK', 'songname': "Going Dumb"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Kaskade & WILL K - Flip Reset [Monstercat Release]"), {'artist': 'Kaskade & WILL K', 'songname': "Flip Reset"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Regard - Ride It (Official Video)"), {'artist': 'Regard', 'songname': "Ride It"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Ed Sheeran - Nancy Mulligan [Official Audio]"), {'artist': 'Ed Sheeran', 'songname': "Nancy Mulligan"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Ed Sheeran - Bad Habits [Official Video]"), {'artist': 'Ed Sheeran', 'songname': "Bad Habits"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Selena Gomez & The Scene - Love You Like A Love Song"), {'artist': 'Selena Gomez & The Scene', 'songname': "Love You Like A Love Song"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Marwa Loud - Bad Boy (Clip Officiel)"), {'artist': 'Marwa Loud', 'songname': "Bad Boy"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Maroon 5 - Lost (Official Music Video)"), {'artist': 'Maroon 5', 'songname': "Lost"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Badshah - Fly | Shehnaaz Gill | Uchana Amit | D Soldierz | Official Video 2021"), {'artist': 'Badshah', 'songname': "Fly"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Taylor Swift - Delicate"), {'artist': 'Taylor Swift', 'songname': "Delicate"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("ZAYN, Taylor Swift - I Don’t Wanna Live Forever (Fifty Shades Darker)"), {'artist': 'ZAYN, Taylor Swift', 'songname': "I Don’t Wanna Live Forever"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Taylor Swift - Bad Blood ft. Kendrick Lamar"), {'artist': 'Taylor Swift', 'songname': "Bad Blood"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Demi Lovato - Confident (Official Video)"), {'artist': 'Demi Lovato', 'songname': "Confident"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("The Weeknd & Ariana Grande - Save Your Tears (Remix) (Official Video)"), {'artist': 'The Weeknd & Ariana Grande', 'songname': "Save Your Tears"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Sean Paul - No Lie ft. Dua Lipa"), {'artist': 'Sean Paul', 'songname': "No Lie"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("PUBLIC - Make You Mine (Put Your Hand in Mine) [Official Video]"), {'artist': 'PUBLIC', 'songname': "Make You Mine"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Selena Gomez - Back To You (13 Reasons Why)"), {'artist': 'Selena Gomez', 'songname': "Back To You"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Kygo, Selena Gomez - It Ain't Me (Official Video)"), {'artist': 'Kygo, Selena Gomez', 'songname': "It Ain't Me"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Alan Walker - Faded"), {'artist': 'Alan Walker', 'songname': "Faded"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("The Kid LAROI, Justin Bieber - STAY (Official Video)"), {'artist': 'The Kid LAROI, Justin Bieber', 'songname': "STAY"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Marshmello x Pritam - BIBA feat. Shirley Setia & Shah Rukh Khan (Official Music Video)"), {'artist': 'Marshmello x Pritam', 'songname': "BIBA"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("GAYLE - abcdefu (Official Music Video)"), {'artist': 'GAYLE', 'songname': "abcdefu"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Bella Poarch - Build a B*tch (Official Music Video)"), {'artist': 'Bella Poarch', 'songname': "Build a B*tch"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Sub Urban & Bella Poarch - INFERNO (Official Music Video)"), {'artist': 'Sub Urban & Bella Poarch', 'songname': "INFERNO"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Tesher x Jason Derulo - Jalebi Baby (Official Video)"), {'artist': 'Tesher x Jason Derulo', 'songname': "Jalebi Baby"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("DJ Snake, J Balvin, Tyga - Loco Contigo"), {'artist': 'DJ Snake, J Balvin, Tyga', 'songname': "Loco Contigo"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("DJ Snake - Taki Taki ft. Selena Gomez, Ozuna, Cardi B (Official Music Video)"), {'artist': 'DJ Snake', 'songname': "Taki Taki"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Shakira - Waka Waka (This Time for Africa) (The Official 2010 FIFA World Cup™ Song)"), {'artist': 'Shakira', 'songname': "Waka Waka"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Alan Walker - Sing Me To Sleep"), {'artist': "Alan Walker", 'songname': "Sing Me To Sleep"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("One Direction - What Makes You Beautiful (Official Video)"), {'artist': "One Direction", 'songname': "What Makes You Beautiful"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Katy Perry - Dark Horse (Official) ft. Juicy J"), {'artist': "Katy Perry", 'songname': "Dark Horse"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit('Skrillex and Diplo - "Where Are Ü Now" with Justin Bieber (Official Video)'), {'artist': "Skrillex and Diplo", 'songname': "Where Are Ü Now"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Adele - Someone Like You (Official Music Video)"), {'artist': "Adele", 'songname': "Someone Like You"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Ed Sheeran - Thinking Out Loud (Official Music Video)"), {'artist': "Ed Sheeran", 'songname': "Thinking Out Loud"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Ellie Goulding - Love Me Like You Do (Official Video)"), {'artist': "Ellie Goulding", 'songname': "Love Me Like You Do"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Silentó - Watch Me (Whip/Nae Nae) (Official)"), {'artist': "Silentó", 'songname': "Watch Me"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Miley Cyrus - Wrecking Ball (Official Video)"), {'artist': "Miley Cyrus", 'songname': "Wrecking Ball"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Ariana Grande ft. Nicki Minaj - Side To Side (Official Video) ft. Nicki Minaj"), {'artist': "Ariana Grande", 'songname': "Side To Side"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Mike Posner - I Took A Pill In Ibiza (Seeb Remix) (Explicit)"), {'artist': "Mike Posner", 'songname': "I Took A Pill In Ibiza"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Pitbull - Timber (Official Video) ft. Ke$ha"), {'artist': "Pitbull", 'songname': "Timber"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Lady Gaga - Bad Romance (Official Music Video)"), {'artist': "Lady Gaga", 'songname': "Bad Romance"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Eminem - Not Afraid (Official Video)"), {'artist': "Eminem", 'songname': "Not Afraid"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Fifth Harmony - Worth It (Official Video) ft. Kid Ink"), {'artist': "Fifth Harmony", 'songname': "Worth It"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Justin Bieber - Baby (Official Music Video) ft. Ludacris"), {'artist': "Justin Bieber", 'songname': "Baby"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Justin Bieber - What Do You Mean? (Official Music Video)"), {'artist': "Justin Bieber", 'songname': "What Do You Mean?"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Ellie Goulding - Burn (Official Video)"), {'artist': "Ellie Goulding", 'songname': "Burn"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Taylor Swift - Bad Blood ft. Kendrick Lamar"), {'artist': "Taylor Swift", 'songname': "Bad Blood"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("MAGIC! - Rude (Official Video)"), {'artist': "MAGIC!", 'songname': "Rude"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Martin Garrix - Animals (Official Video)"), {'artist': "Martin Garrix", 'songname': "Animals"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Drake - Hotline Bling"), {'artist': "Drake", 'songname': "Hotline Bling"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Bruno Mars - The Lazy Song (Official Music Video)"), {'artist': "Bruno Mars", 'songname': "The Lazy Song"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Calvin Harris & Disciples - How Deep Is Your Love"), {'artist': "Calvin Harris & Disciples", 'songname': "How Deep Is Your Love"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Justin Bieber - Love Yourself (Official Music Video)"), {'artist': "Justin Bieber", 'songname': "Love Yourself"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Sia - Elastic Heart feat. Shia LaBeouf & Maddie Ziegler (Official Video)"), {'artist': "Sia", 'songname': "Elastic Heart"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("OneRepublic - Counting Stars (Official Music Video)"), {'artist': "OneRepublic", 'songname': "Counting Stars"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Carly Rae Jepsen - Call Me Maybe"), {'artist': "Carly Rae Jepsen", 'songname': "Call Me Maybe"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("The Weeknd - The Hills (Official Video)"), {'artist': "The Weeknd", 'songname': "The Hills"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Gotye - Somebody That I Used To Know (feat. Kimbra) [Official Music Video]"), {'artist': "Gotye", 'songname': "Somebody That I Used To Know"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Jessie J, Ariana Grande, Nicki Minaj - Bang Bang (Official Video)"), {'artist': "Jessie J, Ariana Grande, Nicki Minaj", 'songname': "Bang Bang"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Ariana Grande - Break Free ft. Zedd"), {'artist': "Ariana Grande", 'songname': "Break Free"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Shakira - Can't Remember to Forget You (Official Video) ft. Rihanna"), {'artist': "Shakira", 'songname': "Can't Remember to Forget You"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Shakira - La La La (Brazil 2014) ft. Carlinhos Brown"), {'artist': "Shakira", 'songname': "La La La"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Jason Derulo - Wiggle feat. Snoop Dogg [Official Music Video]"), {'artist': "Jason Derulo", 'songname': "Wiggle"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("One Direction - What Makes You Beautiful (Official Video)"), {'artist': "One Direction", 'songname': "What Makes You Beautiful"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Katy Perry - Last Friday Night (T.G.I.F.) (Official Music Video)"), {'artist': "Katy Perry", 'songname': "Last Friday Night"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Calvin Harris - Summer (Official Video)"), {'artist': "Calvin Harris", 'songname': "Summer"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Pitbull - Rain Over Me ft. Marc Anthony"), {'artist': "Pitbull", 'songname': "Rain Over Me"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("MACKLEMORE & RYAN LEWIS - THRIFT SHOP FEAT. WANZ (OFFICIAL VIDEO)"), {'artist': "MACKLEMORE & RYAN LEWIS", 'songname': "THRIFT SHOP"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Rihanna - Work (Explicit) ft. Drake"), {'artist': "Rihanna", 'songname': "Work"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Ariana Grande ft. Iggy Azalea - Problem (Official Video)"), {'artist': "Ariana Grande", 'songname': "Problem"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Katy Perry - Firework (Official Music Video)"), {'artist': "Katy Perry", 'songname': "Firework"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Sia - Chandelier (Official Video)"), {'artist': "Sia", 'songname': "Chandelier"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Eminem - Love The Way You Lie ft. Rihanna"), {'artist': "Eminem", 'songname': "Love The Way You Lie"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Rihanna - Diamonds"), {'artist': "Rihanna", 'songname': "Diamonds"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Shawn Mendes - Treat You Better"), {'artist': "Shawn Mendes", 'songname': "Treat You Better"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Avicii - Wake Me Up (Official Video)"), {'artist': "Avicii", 'songname': "Wake Me Up"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Adele - Rolling in the Deep (Official Music Video)"), {'artist': "Adele", 'songname': "Rolling in the Deep"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("David Guetta - Hey Mama (Official Video) ft Nicki Minaj, Bebe Rexha & Afrojack"), {'artist': "David Guetta", 'songname': "Hey Mama"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Pharrell Williams - Happy (Video)"), {'artist': "Pharrell Williams", 'songname': "Happy"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Sia - Cheap Thrills (Lyric Video) ft. Sean Paul"), {'artist': "Sia", 'songname': "Cheap Thrills"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Calvin Harris - This Is What You Came For (Official Video) ft. Rihanna"), {'artist': "Calvin Harris", 'songname': "This Is What You Came For"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Iggy Azalea - Fancy ft. Charli XCX (Official Music Video)"), {'artist': "Iggy Azalea", 'songname': "Fancy"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Sam Smith - I'm Not The Only One (Official Video)"), {'artist': "Sam Smith", 'songname': "I'm Not The Only One"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Fifth Harmony - Work from Home (Official Video) ft. Ty Dolla $ign"), {'artist': "Fifth Harmony", 'songname': "Work from Home"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Naughty Boy - La la la ft. Sam Smith (Official Video)"), {'artist': "Naughty Boy", 'songname': "La la la"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("John Legend - All of Me (Official Video)"), {'artist': "John Legend", 'songname': "All of Me"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Jennifer Lopez - On The Floor ft. Pitbull"), {'artist': "Jennifer Lopez", 'songname': "On The Floor"}): count += 1
    except:
      pass

    try:
      if test(SongNameSplit.namesplit("Bruno Mars - Just The Way You Are (Official Music Video)"), {'artist': "Bruno Mars", 'songname': "Just The Way You Are"}): count += 1
    except:
      pass

    endTime = time.perf_counter()

    fails = totaltests - count

    print("Correct: ", count)
    print("Fails: ", fails)

    print("Accuracy: ", (count/totaltests)*100)

    print("Time taken (in seconds): ", endTime - startTime)

   
## 96.8% Accurate (In my test on version 2.1.2)

runTests()
