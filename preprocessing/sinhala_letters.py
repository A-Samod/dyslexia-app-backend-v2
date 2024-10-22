sinhala_letters = [
    'අ', 'ආ', 'ඇ', 'ඈ', 'ඉ', 'ඊ', 'උ', 'එ', 'ඒ', 'ඔ', 'ඕ', 'ක', 'කා', 'කැ', 'කෑ',
    'කි', 'කී', 'කු', 'කූ', 'ක්', 'කා්', 'ක්‍ර', 'ක්‍රි', 'ක්‍රී', 'ග', 'ගා', 'ගැ', 'ගෑ', 'ගි', 'ගී',
    'ගු', 'ගූ', 'ග්', 'ගා්', 'ග්‍ර', 'ග්‍රි', 'ග්‍රී', 'ච', 'චා', 'චැ', 'චෑ', 'චි', 'චී', 'චු', 'චූ',
    'ච්', 'චා්', 'ච්‍ර', 'ච්‍රි', 'ච්‍රී', 'ජ', 'ජා', 'ජැ', 'ජෑ', 'ජි', 'ජී', 'ජු', 'ජූ', 'ජ්', 'ජා්',
    'ජ්‍ර', 'ජ්‍රි', 'ජ්‍රී', 'ට', 'ටා', 'ටැ', 'ටෑ', 'ටි', 'ටී', 'ටු', 'ටූ', 'ට්', 'ටා්', 'ට්‍ර', 'ට්‍ර්',
    'ට්‍රි', 'ඩ', 'ඩා', 'ඩැ', 'ඩෑ', 'ඩි', 'ඩී', 'ඩු', 'ඩූ', 'ඩ්', 'ඩා්', 'ඩ්‍ර', 'ඩ්‍ර්', 'ඩ්‍රි', 'ණ',
    'ණා', 'ණි', 'ත', 'තා', 'ති', 'තී', 'තු', 'තූ', 'ත්', 'තා්', 'ත්‍ර', 'ත්‍රා', 'ත්‍රි', 'ත්‍රී', 'ද', 
    'දා', 'දැ', 'දෑ', 'දි', 'දී', 'දු', 'දූ', 'ද්', 'දා්', 'ද්‍ර', 'ද්‍රා්', 'ද්‍රා', 'ද්‍රි', 'ද්‍රී', 'න',
    'නා', 'නැ', 'නෑ', 'නි', 'නී', 'නු', 'නූ', 'න්', 'නා්', 'න්‍ර', 'න්‍රා', 'න්‍රි', 'න්‍රී', 'ප', 'පා',
    'පැ', 'පෑ', 'පි', 'පී', 'පු', 'පූ', 'ප්', 'ප්‍රෝ', 'පා්', 'ප්‍ර', 'ප්‍රා', 'ප්‍රි', 'ප්‍රී', 'බ', 'බා',
    'බැ', 'බෑ', 'බි', 'බී', 'බු', 'බූ', 'බ්', 'බා්', 'බ්‍ර', 'බ්‍රා', 'බ්‍රි', 'බ්‍රී', 'බ්‍රා්', 'ම', 'මා',
    'මැ', 'මෑ', 'මි', 'මී', 'මු', 'මූ', 'ම්', 'මා්', 'ම්‍ර', 'ම්‍රා', 'ම්‍රි', 'ම්‍රී', 'ම්‍රා්', 'ය', 'යා',
    'යැ', 'යෑ', 'යි', 'යී', 'යු', 'යූ', 'ා්', 'ය්', 'යා්', 'ර', 'රා', 'රැ', 'රෑ', 'රු', 'රූ',
    'රි', 'රී', 'ල', 'ලා', 'ලැ', 'ලෑ', 'ලි', 'ලී', 'ලු', 'ලූ', 'ල්', 'ලා්',  'ව' ,'වා', 'වැ',
    'වෑ', 'වි', 'වී', 'වු', 'වූ', 'ව්', 'වා්', 'ව්‍ර', 'ව්‍රා', 'ව්‍රැ', 'ව්‍රෑ', 'ව්‍රා්', 'ශ', 'ශා', 'ශැ',
    'ශෑ', 'ශි', 'ශී', 'ශු', 'ශූ', 'ශ්', 'ශා්', 'ශ්‍ර', 'ශ්‍රා', 'ශ්‍රැ', 'ශ්‍රෑ', 'ශ්‍රි', 'ශ්‍රී', 'ශ්‍රා්', 'ෂ',
    'ෂ', 'ෂා', 'ෂැ', 'ෂෑ', 'ෂි', 'ෂී', 'ෂු', 'ෂූ', 'ෂ්', 'ෂා්', 'ස', 'සා', 'සැ', 'සෑ', 'සි', 'සී', 
    'සු', 'සූ', 'සා්', 'ස්‍ර', 'ස්‍රා', 'ස්‍රි', 'ස්‍රී', 'ස්', 'හ', 'හා', 'හැ', 'හෑ', 'හි', 'හී', 'හු',
    'හූ', 'හ්', 'හා්', 'ළ', 'ළා', 'ළැ', 'ළෑ', 'ළි', 'ළී', 'එැ', 'එෑ', 'ෆ', 'ෆා', 'ෆැ', 'ෆෑ',
    'ෆි', 'ෆී', 'ෆු', 'ෆූ', 'ෆ්‍ර', 'ෆ්‍රි', 'ෆ්‍රී', 'ෆ්‍රැ', 'ෆ්‍රෑ', 'ෆ්', 'ෆා්', 'ක්‍රා', 'ක්‍රැ', 'ක්‍රෑ', 'ක්‍රා්',
    'ග්‍රා්', 'ඛ', 'ඛා', 'ඛි', 'ඛී', 'ඛ්', 'ඝ', 'ඝා', 'ඝැ', 'ඝෑ', 'ඝි', 'ඝී', 'ඝු', 'ඝූ', 'ඝා්',
    'ඝ්', 'ඝ්‍ර', 'ඝ්‍රා', 'ඝ්‍රි', 'ඝ්‍රී', 'ඳ', 'ඳා', 'ඳැ', 'ඳෑ', ' ෑ', 'ඳි', 'ඳී', 'ඳු', 'ඳූ', 'ඳා්',
    'ඳ්', 'ඟ', 'ඟා', 'ඟැ', 'ඟෑ', 'ඟි', 'ඟී', 'ඟු', 'ඟූ', 'ඟා්', 'ඟ්', 'ඬ ැ', 'ඬා', 'ඬැ',
    'ඬෑ', 'ඬි', 'ඬී', 'ඬු', 'ඬූ', 'ඬා්', 'ඬ්', 'ඹ', 'ඹා', 'ඹැ', 'ඹෑ', 'ඹි', 'ඹී', 'ඹු', 'ඹූ',
    'ඹා්', 'ඹ්', 'භ', 'භා', 'භැ', 'භෑ', 'භි', 'භී', 'භු', 'භූ', 'භා්', 'භ්', 'ධ', 'ධා', 'ධැ',
    'ධෑ', 'ධි', 'ධී', 'ධු', 'ධූ', 'ධා්', 'ධ්', 'ඨ', 'ඨා', 'ඨැ', 'ඨි', 'ඨී', 'ඨු', 'ඨූ', 'ඨ්',
    'ඪ', 'ඪා', 'ඪි', 'ඩා්', 'ඵ', 'ඵා', 'ඵු', 'ඵි', 'ඵා්', 'ඵ්', 'ථ', 'ථා', 'ථැ', 'ථ්', ' ා',
    'ෟ', 'ණැ', 'ණෑ', 'ෘ', 'ණී', 'ණු', 'ණූ', 'ණා්', 'ණ්', 'ඥ', 'ඥා', 'ඥා්', 'ඤ', 'ඤා', 'ඤු',
    'ඤා්', 'ඤ්', 'ඣ', 'ඣා', 'ඣු', 'ඣා්', 'ඣ්', 'ඦ', 'ඦා', 'ඦැ', 'ඦෑ', 'ඦි', 'ඦු', 'ඦූ', 'ඦෝ',
    'ඦ්', 'ඡ', 'ඡා', 'ඡැ', 'ඡෑ', 'ඡි', 'ඡේ', 'තැ', 'තෑ', 'ත්‍රැ', 'ත්‍රෑ', 'ත්‍රා්', 'ළු', 'ෲ', '‍‍්‍යු',
    'ෛ', 'ෙ', '‍්‍ය', '‍‍්‍යූ'
]

# sinhala_letters = [
#     'අ', 'ආ', 'ඇ', 'ඈ', 'ඉ', 'ඊ', 'උ', 'එ', 'ඒ', 'ඔ', 'ඕ', 'ක','ග','ච','ජ','ට','ඩ','ත','ද', 
#     'න', 'ප', 'බ', 'ම', 'ය', 'ර','ල', 'ව' ,'වා','ස', 'හ','ළ'
# ]