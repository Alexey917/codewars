'''You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
Examples:

strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).
Note

consecutive strings : follow one after another without an interruption
'''


def longest_consec(strarr, k):
    if len(strarr) == 0 or len(strarr) < k or k <= 0:
        return ''

    longest_str = [strarr[i] + "".join(strarr[i+1:i+k]) if i != len(strarr)-1 else strarr[i]
                   for i in range(len(strarr))
                   ]

    print(longest_str)

    maximum = ''

    for i in longest_str:
        if len(maximum) < len(i):
            maximum = i
    return maximum


print(longest_consec(['xxxhhhvvvssjj', 'lllaaaffgggcccjjffq', 'fcccdxpoooiiif', 'qqjfmmydd', 'uujjttmmoonnjjj', 'fffiihgg', 'tttllrriiidxxss', 'uuubqqqbcccf', 'ssscfk', 'ssddxaaaggjqfff', 'urrrgghhhnnnijppp', 'ooodddrnnu', 'uuqgwwbpf', 'tcczvwd', 'ddddwwwwwp', 'wwvaaffflllqmdddd', 'bbblluyyvzz', 'uuppammm', 'bbvvvccco', 'rrkkjyyyx', 'vvxbbehhkk', 'aaeeezzzjjjaaagzz', 'llcczzzyjtbb', 'llzzzpppdd', 'iffgzzbbjjj', 'hhhzzzusss', 'vxcccjjjm', 'vvvllttcbshh', 'bbhhhppd', 'rrrggknnneee', 'qrgggjtcccjjj', 'ooaarsss', 'zzlllzzbb', 'jjjwdwwwmmkddd', 'pppjjjkk', 'iiiiiiutuuuaa', 'gggbxxxxvveee', 'fssiii', 'vwwqk', 'kipppgnnnookkk', 'qqzrbyysss', 'ddnnwwwuuummmnn', 'wwwppgxxqqggg', 'yhhytt', 'dddttp', 'teiinnyrrrxxx', 'oockkmmoonnn', 'ssshoxxxmmhr', 'mmmhz', 'hhssswwweejjjnn', 'ivvbbff', 'ppphcccgoo', 'iiiezzzbbb', 'mmmnntthecc', 'llaaiissoookk', 'qsssppaaggjjsssi', 'wwyyxxgii', 'xmmmnnngg', 'wwbbbii', 'aabbpppoosssdluuu', 'vvvvnnnxxzzzggg', 'kcccyqq', 'uuunooopiro', 'jynnnaacw', 'oonnwwwkddd', 'ynjjttrrrd', 'lllrrrvvvvms', 'lllzlsss', 'rrppgggrrdd', 'uaaaall', 'aamvvvvv', 'mmtssvvvxxrr', 'qzisp', 'fffbbggaaaaattr', 'gpxxxmmmttdvvvmmm', 'wixz', 'qqqttuuurrrrr', 'oosssvvzff', 'gggckkkmmmtt', 'aaooooorrruuiir', 'zctlsyy', 'tiiyyjjcc', 'mevvtty', 'wtthhznn', 'ppqqdd', 'krrppkkbnndd', 'aaawwwnnltuuppp', 'iiiyddfftttkmmm', 'vvviieeekkkoo', 'oppbswwwtttnaaaw', 'dddyyynnvnkkkcc', 'ssseeeffdddfffwww', 'qqqtvvv', 'zjjc', 'wwppmmbbb', 'fskkkheegggx', 'lllywwwaayyyggvvv', 'nnndddttbbbfffccc', 'xnnrrubbb', 'qqhhnnncccglllrrr', 'mmmeeffuuullseeo', 'jjjrrxhhrrryy', 'xxiivvjjsss', 'bgggfbb', 'ppjjjnnjsjjms', 'oossmmrofffvvvzzz', 'xxxootbrfff', 'eeaaaoooyexxx', 'ciwiiii', 'pppkf', 'ovqqqrcyyvvv', 'wdddee', 'ffkkknbbyyyvvvttt', 'savvwbrrraaai', 'kdbbb', 'bbottvvvw', 'aaattcccllddnnfr', 'jgggqzznneevyy', 'ttvviiibbddd', 'eezddplluuu', 'xxxbvvvnngyyy', 'dddgkkkprrr', 'ahhqqnaaa', 'ttlddpppullggaaa', 'aammdf', 'qqatttyymmm', 'ggiinnvx', 'fffvvvlibbbbbw', 'peeeeeetttee', 'ffrwwee', 'lllddttpppfffiijjj', 'duuuqzppx', 'xyyyrrr', 'jjjtaaauuggooo', 'jjjoooddmmmv', 'rriimmnl', 'ffimmmcc', 'pkky', 'urrrwwoo', 'puurrrggbbeeeuuu', 'ddooewpfffqqqoo', 'lwwwwwwkuuu', 'aaaiiirrrbbeee', 'reeedddggssvv', 'xlllzzzl', 'xxxaammss', 'rnnuudddggwwwz', 'ssjjjrtttvvd', 'xxxxxivvvooo', 'krrgbbbyygggtttggtt', 'qmqqqyyyjjjvtoofff', 'hhmmuqq', 'jjhhhjjrrttt', 'etfgmoo', 'rrrwwjjff', 'heerooofftttkkkiiy', 'mmjjjxxssfff', 'mmmaamtttmm'], k = 121))

