<div align="center">
  <img src="./assets/banner.png" />
</div>

# The Doki Doki Literature Club API

[![CI](https://github.com/UltiRequiem/ddlc_api/actions/workflows/ci.yml/badge.svg)](https://github.com/UltiRequiem/ddlc_api/actions/workflows/ci.yml)

A RESTful API based on [Doki Doki Literature Club](https://ddlc.moe), The #1
Psychological Horror Experience.

This API is still in constant development so if you have any idea of a feature
that you would like the api to have, open an issue or make a pull request.

## Endpoints

### `GET /`

> https://ddlcapi.herokuapp.com

Returns an object containing the data of all the characters and poems.

<details>
  <summary>Response</summary>

```json
{
  "characters": [
    {
      "name": "yuri",
      "age": 18,
      "born_date": "December 10th",
      "concept_height": "165 cm",
      "gender": "Female",
      "hair_color": "Dark Purple",
      "eye_color": "Light Purple",
      "filename": "yuri.chr",
      "appears": ["Act 1", "Act 2", "Act 4"],
      "voice_actor": null,
      "illustration": "https://ddlcapi.herokuapp.com/illustrations/yuri.png"
    },
    {
      "name": "monika",
      "age": 18,
      "born_date": "September 22nd",
      "concept_height": "160 cm",
      "gender": "Female",
      "hair_color": "Coral Brown",
      "eye_color": "Emerald Green",
      "filename": "monika.chr",
      "appears": ["Act 1", "Act 2", "Act 3", "Act 4"],
      "voice_actor": "Jillian Ashcraft",
      "illustration": "https://ddlcapi.herokuapp.com/illustrations/monika.png"
    },
    {
      "name": "natsuki",
      "age": 18,
      "born_date": "December 10th",
      "concept_height": "150 cm",
      "gender": "Female",
      "hair_color": "Pastel Pink",
      "eye_color": "Pink",
      "filename": "natsuki.chr",
      "appears": ["Act 1", "Act 2", "Act 4"],
      "voice_actor": null,
      "illustration": "https://ddlcapi.herokuapp.com/illustrations/natsuki.png"
    },
    {
      "name": "sayori",
      "age": 18,
      "born_date": "April 13",
      "concept_height": "157 cm",
      "gender": "Female",
      "hair_color": "Coral Pink",
      "eye_color": "Sky Blue",
      "filename": "sayori.chr",
      "appears": ["Act 1", "Act 4"],
      "voice_actor": null,
      "illustration": "https://ddlcapi.herokuapp.com/illustrations/sayori.png"
    }
  ],
  "poems": [
    {
      "author": "monika",
      "act_1": [
        {
          "title": "Hole in Wall",
          "occasion": "This poem is shown on the second day.",
          "body": "It couldn't have been me. \nSee, the direction the spackle protrudes.\nA noisy neighbor? An angry boyfriend? I'll never know. I wasn't home.\nI peer inside for a clue.\nNo! I can't see. I reel, blind, like a film left out in the sun.\nBut it's too late. My retinas.\nAlready scorched with a permanent copy of the meaningless image.\nIt's just a little hole. It wasn't too bright.\nIt was too deep.\nStretching forever into everything.\nA hole of infinite choices.\nI realize now, that I wasn't looking in.\nI was looking out.\nAnd he, on the other side, was looking in.",
          "translation": null
        },
        {
          "title": "Save Me",
          "occasion": "This poem is shown on the third day.",
          "body": "The colors, they won't stop.\nBright, beautiful colors\nFlashing, expanding, piercing\nRed, green, blue\nAn endless\ncacophony\nOf meaningless\nnoise\n\nThe noise, it won't stop.\nViolent, grating waveforms\nSqueaking, screeching, piercing\nSine, cosine, tangent\nLike playing a chalkboard on a turntable\nLike playing a vinyl on a pizza crust\nAn endless\npoem\nOf meaningless\n\nLoad Me",
          "translation": null
        },
        {
          "title": "The Lady who Knows Everything",
          "occasion": "This poem is shown on the fourth day.",
          "body": "Day after day, I search.\nI search with little hope, knowing legends don't exist.\nBut when all else has failed me,\nWhen all others have turned away,\nThe legend is all that remains – the last dim star glimmering in the twilit sky.\n\nUntil one day, the wind ceases to blow.\nI fall.\nAnd I fall and fall, and fall even more.\nGentle as a feather.\nA dry quill, expressionless.\n\nBut a hand catches me, between the thumb and forefinger.\nThe hand of a beautiful lady.\nI look at her eyes and find no end to her gaze.\n\nThe Lady who Knows Everything knows what I am thinking.\nBefore I can speak, she responds in a hollow voice.\nI have found every answer, all of which amount to nothing.\nThere is no meaning.\nThere is no purpose.\nAnd we seek only the impossible.\nI am not your legend.\nYour legend does not exist.\n\nAnd with a breath, she blows me back afloat, and I pick up a gust of wind.",
          "translation": null
        }
      ],
      "act_2": [
        {
          "title": "Hole in Wall (2)",
          "occasion": "This poem is shown on the second day.",
          "body": "But he wasn't looking at me.\nConfused, I frantically glance at my surroundings.\nBut my burned eyes can no longer see color.\nAre there others in this room? Are they talking?\nOr are they simply poems on flat sheets of paper,\nThe sound of frantic scrawling playing tricks on my ears?\nThe room begins to crinkle.\nClosing in on me.\nThe air I breathe dissipate before it reaches my lungs.\nI panic. There must be a way out.\nIt's right there. He's right there.\n\nSwallowing my fears, I brandish my pen.",
          "translation": null
        },
        {
          "title": "Save Me(2)",
          "occasion": "This poem is shown on the third day.",
          "body": "The colors, they won't\nBright, bea t ful c l rs\nFlash ng, exp nd ng, piercing\nRed, green, blue\nAn ndless\nCACOPHONY\nOf meaningless\nnoise\n\nThe noise, it won't STOP.\nViol nt, grating w vef rms\nSq e king, screech ng, piercing\nSINE, COSINE, TANGENT\nLike play ng a ch lkboard on a t rntable\nLike playing a KNIFE on a BREATHING RIBCAGE\nn ndl ss\np m\nOf m n ngl ss\n\nDelete Her",
          "translation": null
        }
      ],
      "act_3": [
        {
          "title": "Happy End",
          "occasion": "This poem is shown during Monika's initial dialogue in Act 3.",
          "body": "Pen in hand, I find my strength.\nThe courage endowed upon me by my one and only love.\nTogether, let us dismantle this crumbling world\nAnd write a novel of our own fantasies.\n\nWith a flick of her pen, the lost finds her way.\nIn a world of infinite choices, behold this special day.\n\nAfter all,\nNot all good times must come to an end",
          "translation": null
        }
      ]
    },
    {
      "author": "natsuki",
      "act_1": [
        {
          "title": "Eagles Can Fly",
          "occasion": "This poem is shown on the second day.",
          "body": "Monkeys can climb\nCrickets can leap\nHorses can race\nOwls can seek\nCheetahs can run\nEagles can fly\nPeople can try\nBut that's about it.",
          "translation": null
        },
        {
          "title": "Amy Likes Spiders",
          "occasion": "This poem is shown on the third day.",
          "body": "You know what I heard about Amy?\nAmy likes spiders.\nIcky, wriggly, hairy, ugly spiders!\nThat's why I'm not friends with her.\n\nAmy has a cute singing voice.\nI heard her singing my favorite love song.\nEvery time she sang the chorus, my heart would pound to the rhythm of the words.\nBut she likes spiders.\nThat's why I'm not friends with her.\n\nOne time, I hurt my leg really bad.\nAmy helped me up and took me to the nurse.\nI tried not to let her touch me.\nShe likes spiders, so her hands are probably gross.\nThat's why I'm not friends with her.\n\nAmy has a lot of friends.\nI always see her talking to people.\nShe probably talks about spiders.\nWhat if her friends start to like spiders too?\nThat's why I'm not friends with her.\n\nIt doesn't matter if she has other hobbies.\nIt doesn't matter if she keeps it private.\nIt doesn't matter if it doesn't hurt anyone.\n\nIt's gross.\nShe's gross.\nThe world is better off without spider lovers.\n\nAnd I'm gonna tell everyone.",
          "translation": null
        },
        {
          "title": "Because You",
          "occasion": "This poem is shown on the fourth day, if the player made three poems that appeal to Natsuki.",
          "body": "Tomorrow will be brighter with me around\nBut when today is dim, I can only look down.\nMy looking is a little more forward\nBecause you look at me.\n\nWhen I want to say something, I say it with a shout!\nBut my truest feelings can never come out.\nMy words are a little less empty\nBecause you listen to me.\n\nWhen something is above me, I reach for the stars.\nBut when I feel small, I don't get very far.\nMy standing is a little bit taller\nBecause you sit with me.\n\nI believe in myself with all of my heart.\nBut what do I do when it's torn all apart?\nMy faith is a little bit stronger\nBecause you trusted me.\n\nMy pen always puts my feelings to the test.\nI'm not a good writer, but my best is my best.\nMy poems are a little bit dearer\nBecause you think of me.\n\nBecause you, because you, because you.",
          "translation": null
        },
        {
          "title": "I'll Be Your Beach",
          "occasion": "This poem is shown on the fourth day, if the player didn't make three poems that appeal to Natsuki.",
          "body": "Your mind is so full of troubles and fears\nThat diminished your wonder over the years\nBut today I have a special place\nA beach for us to go.\n\nA shore reaching beyond your sight\nA sea that sparkles with brilliant light\nThe walls in your mind will melt away\nBefore the sunny glow.\n\nI'll be the beach that washes your worries away\nI'll be the beach that you daydream about each day\nI'll be the beach that makes your heart leap\nIn a way you thought had left you long ago.\n\nLet's bury your heavy thoughts in a pile of sand\nBathe in sunbeams and hold my hand\nWash your insecurities in the salty sea\nAnd let me see you shine.\n\nLet's leave your memories in a footprint trail\nSet you free in my windy sail\nAnd remember the reasons you're wonderful\nWhen you press your lips to mine.\n\nI'll be the beach that washes your worries away\nI'll be the beach that you daydream about each day\nI'll be the beach that makes your heart leap\nIn a way you thought had left you long ago.\n\nBut if you let me by your side\nYour own beach, your own escape\nYou'll learn to love yourself again.",
          "translation": null
        }
      ],
      "act_2": [
        {
          "title": "T3BlbiBZb3VyIFRoaXJkIEV5ZQ==",
          "occasion": "This poem (written in Base64 code) is shown on the third day, if the player made two poems that appeal to Natsuki.",
          "body": "SSBjYW4gZmVlbCB0aGUgdGVuZGVybmVz\ncyBvZiBoZXIgc2tpbiB0aHJvdWdoIHRo\nZSBrbmlmZSwgYXMgaWYgaXQgd2VyZSBh\nbiBleHRlbnNpb24gb2YgbXkgc2Vuc2Ug\nb2YgdG91Y2guIE15IGJvZHkgbmVhcmx5\nIGNvbnZ1bHNlcy4gVGhlcmUncyBzb21l\ndGhpbmcgaW5jcmVkaWJseSBmYWludCwg\nZGVlcCBkb3duLCB0aGF0IHNjcmVhbXMg\ndG8gcmVzaXN0IHRoaXMgdW5jb250cm9s\nbGFibGUgcGxlYXN1cmUuIEJ1dCBJIGNh\nbiBhbHJlYWR5IHRlbGwgdGhhdCBJJ20g\nYmVpbmcgcHVzaGVkIG92ZXIgdGhlIGVk\nZ2UuIEkgY2FuJ3QuLi5JIGNhbid0IHN0\nb3AgbXlzZWxmLg==",
          "translation": {
            "title": "Open Your Third Eye",
            "body": "I can feel the tenderness of her skin through the knife, as if it were an extension of my sense of touch. My body nearly convulses. There's something incredibly faint, deep down, that screams to resist this uncontrollable pleasure. But I can already tell that I'm being pushed over the edge. I can't... I can't stop myself."
          }
        },
        {
          "title": "Natsuki's Request (No Title)",
          "occasion": "This poem is shown on the fourth day.",
          "body": "I don't know how else to bring this up. But there's been something\nI've been worried about. Yuri has been acting kind of strange lately.\nYou've only been here a few days, so you may not know what I mean. But\nshe's not normally like this. She's always been quiet and polite and\nattentive...things like that.\n\nOkay... This is really embarrassing, but I'm forcing myself to\nsuck it up. The truth is, I'm REALLY worried about her. But if I try\ntalking to her, she'll just get mad at me again. I don't know what to\ndo. I think you're the only person that she'll listen to. I don't know\nwhy. But please try to do something. Maybe you can convince her to talk\nto a therapist.\n\nI've always wanted to try being better friends with Yuri, and\nit really hurts me to see this happening. I know I'm going to hate\nmyself later for admitting that, but right now I don't care. I just feel\nso helpless. So please see if you can do something to help. I don't\nwant anything bad to happen to her. I'll make you cupcakes if I have to.\nJust please try to do something.\n\nAs for Monika... I don't know why, but she's been really dismissive about this. It's like she just wants us to ignore it. So I'm mad at her right now, and that's why I'm coming to you about this. DON'T LET HER KNOW I WROTE THIS!!!! Just pretend like I gave you a really good poem, okay? I'm counting on you. Thanks for reading.",
          "translation": null
        }
      ],
      "act_3": null
    },
    {
      "author": "sayori",
      "act_1": [
        {
          "title": "Dear Sunshine",
          "occasion": "This poem is shown on the second day.",
          "body": "The way you glow through my blinds in the morning\nIt makes me feel like you missed me.\nKissing my forehead to help me out of bed.\nMaking me rub the sleepy from my eyes.\n\nAre you asking me to come out and play?\nAre you trusting me to wish away a rainy day?\nI look above. The sky is blue.\nIt's a secret, but I trust you too.\n\nIf it wasn't for you, I could sleep forever.\nBut I'm not mad.\n\nI want breakfast.",
          "translation": null
        },
        {
          "title": "Bottles",
          "occasion": "This poem is shown on the third day.",
          "body": "I pop off my scalp like the lid of a cookie jar.\nIt's the secret place where I keep all my dreams.\nLittle balls of sunshine, all rubbing together like a bundle of kittens.\n\nI reach inside with my thumb and forefinger and pluck one out.\nIt's warm and tingly.\nBut there's no time to waste! I put it in a bottle to keep it safe.\nAnd I put the bottle on the shelf with all of the other bottles.\nHappy thoughts, happy thoughts, happy thoughts in bottles, all in a row.\n\nMy collection makes me lots of friends.\nEach bottle a starlight to make amends.\nSometimes my friend feels a certain way.\nDown comes a bottle to save the day.\n\nNight after night, more dreams.\nFriend after friend, more bottles.\nDeeper and deeper my fingers go.\nLike exploring a dark cave, discovering the secrets hiding in the nooks and crannies.\nDigging and digging.\nScraping and scraping.\n\nI blow dust off my bottle caps.\nIt doesn't feel like time elapsed.\nMy empty shelf could use some more.\nMy friends look through my locked front door.\n\nFinally, all done. I open up, and in come my friends.\nIn they come, in such a hurry. Do they want my bottles that much?\nI frantically pull them from the shelf, one after the other.\nHolding them out to each and every friend.\nEach and every bottle.\nBut every time I let one go, it shatters against the tile between my feet.\nHappy thoughts, happy thoughts, happy thoughts in shards, all over the floor.\n\nThey were supposed to be for my friends, my friends who aren't smiling.\nThey're all shouting, pleading. Something.\nBut all I hear is echo, echo, echo, echo, echo\nInside my head.",
          "translation": null
        },
        {
          "title": "%",
          "occasion": "This poem is shown on the festival day.",
          "body": "Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of\nGet.\nOut.\nOf.\nMy.\nHead.\n\n\nGet out of my head before I do what I know is best for you.\nGet out of my head before I listen to everything she said to me.\nGet out of my head before I show you how much I love you.\nGet out of my head before I finish writing this poem.\n\n\n\nBut a poem is never actually finished.\nIt just stops moving.",
          "translation": null
        }
      ],
      "act_2": null,
      "act_3": null
    },
    {
      "author": "yuri",
      "act_1": [
        {
          "title": "Ghost under the light",
          "occasion": "This poem is shown on the second day.",
          "body": "The tendrils of my hair illuminate beneath the amber glow.\nBathing.\nIt must be this one.\nThe last remaining streetlight to have withstood the test of time.\nThe last yet to be replaced by the sickening blue-green of the future.\nI bathe. Calm; breathing air of the present but living in the past.\nThe light flickers.\nI flicker back.",
          "translation": null
        },
        {
          "title": "The Raccoon",
          "occasion": "This poem is shown on the third day.",
          "body": "It happened in the dead of night while I was slicing bread for a guilty snack.\nMy attention was caught by the scuttering of a raccoon outside my window.\nThat was, I believe, the first time I noticed my strange tendencies as an unordinary\nhuman.\nI gave the raccoon a piece of bread, my subconscious well aware of the consequences.\nWell aware that a raccoon that is fed will always come back for more.\nThe enticing beauty of my cutting knife was the symptom.\nThe bread, my hungry curiosity.\nThe raccoon, an urge.\n\nThe moon increments its phase and reflects that much more light off of my cutting\nknife.\nThe very same light that glistens in the eyes of my raccoon friend.\nI slice the bread, fresh and soft. The raccoon becomes excited.\nor perhaps I'm merely projecting my emotions onto the newly-satisfied animal.\n\nThe raccoon has taken to following me.\nYou could say that we've gotten quite used to each other.\nThe raccoon becomes hungry more and more frequently, so my bread is always handy.\nEvery time I brandish my cutting knife the raccoon shows me its excitement.\nA rush of blood. Classic Pavlovian conditioning. I slice the bread.\n\nAnd I feed myself again.",
          "translation": null
        },
        {
          "title": "Ghost under the Light pt. 2",
          "occasion": "This poem is shown on the fourth day, if the player made three poems that appeal to Yuri.",
          "body": "The tendrils of my hair illuminate beneath the amber glow.\nBathing.\nIn the distance, a blue-green light flickers.\nA lone figure crosses its path– a silhouette obstructing the eerie glow.\nMy heart pounds. The silhouette grows. Closer Closer\nI open my umbrella, casting a shadow to shield me from visibility.\nBut I am too late.\nHe steps into the streetlight. I gasp and drop my umbrella.\nThe light flickers. My heart pounds. He raises his arm.\n\nTime stops.\n\nThe only indication of movement is the amber light flickering against his outstretched\narm.\nThe flickering light is in rhythm with the pounding of my heart.\nTeasing me for succumbing to this forbidden emotion.\nHave you ever heard of a ghost feeling warmth before?\nGiving up on understanding, I laugh.\nUnderstanding is overrated.\nI touch his hand. The flickering stops.\nGhosts are blue-green. My heart is amber.",
          "translation": null
        },
        {
          "title": "Beach",
          "occasion": "This poem is shown on the fourth day, if the player didn't make three poems that appeal to Yuri.",
          "body": "A marvel millions of years in the making.\nWhere the womb of Earth chaotically meets the surface.\nUnder a clear blue sky, an expanse of bliss -\nBut beneath gray rolling clouds, an endless enigma.\nThe easiest world to get lost in\nis one where everything can be found.\n\nOne can only build a sand castle where the sand is wet.\nBut where the sand is wet, the tide comes.\nWill it gently lick at your foundations until you give in?\nOr will a sudden wave send you crashing down in the blink of an eye?\nEither way the outcome is the same.\nYet we still build sand castles.\n\nI stand where the foam wraps around my ankles.\nWhere my toes squish into the sand.\nThe salty air is therapeutic.\nThe breeze is gentle, yet powerful.\nI sink my toes into the ultimate boundary line, tempted by the foamy tendrils.\nTurn back, and I abandon my peace to erode at the shore.\nDrift forward, and I return to Earth forevermore.",
          "translation": null
        }
      ],
      "act_2": [
        {
          "title": "Wheel",
          "occasion": "This poem is shown on the third day.",
          "body": "A rotating wheel. Turning an axle. Grinding. Bolthead. Linear gearbox. Falling sky. Seven holy stakes. A docked ship. A portal to another world. A thin rope tied to a thick rope. A torn harness. Parabolic gearbox. Expanding universe. Time controlled by slipping cogwheels. Existence of God. Swimming with open water in all directions. Drowning. A prayer written in blood. A prayer written in time-devouring snakes with human eyes. A thread connecting all living human eyes. A kaleidoscope of holy stakes. Exponential gearbox. A sky of exploding stars. God disproving the existence of God. A wheel rotating in six dimensions. Forty gears and a ticking clock. A clock that ticks one second for every rotation of the planet. A clock that ticks forty times every time it ticks every second time. A bolthead of holy stakes tied to the existence of a docked ship to another world. A kaleidoscope of blood written in clocks. A time-devouring prayer connecting a sky of forty gears and open human eyes in all directions. Breathing gearbox. Breathing bolthead. Breathing ship. Breathing portal. Breathing snakes. Breathing God. Breathing blood. Breathing holy stakes. Breathing human eyes. Breathing time. Breathing prayer. Breathing sky. Breathing wheel.",
          "translation": null
        },
        {
          "title": "mdpnfbo,jrfp",
          "occasion": "This poem is shown on the fourth day.",
          "body": "ed,,zinger suivante,,tels handknits finish,,cagefuls basinlike bag octopodan,,imbossing vaporettos rorid easygoingnesses nalorphines,,benzol respond washerwomen bristlecone,,parajournalism herringbone farnarkeled,,episodically cooties,,initiallers bimetallic,,leased hinters,,confidence teetotaller computerphobes,,pinnacle exotically overshades prothallia,,posterior gimmickry brassages bediapers countertrades,,haslet skiings sandglasses cannoli,,carven nis egomaniacal,,barminess gallivanted,,southeastward,,oophoron crumped,,tapued noncola colposcopical,,dolente trebbiano revealment,,outworked isotropous monosynaptic excisional moans,,enterocentesis jacuzzi preoccupations,,hippodrome outward googs,,tabbises undulators,,metathesizing,,sharia prepostor,,neuromast curmudgeons actability,,archaise spink reddening miscount,,madmen physostigmin statecraft neurocoeles bammed,,tenderest barguests crusados trust,,manshifts darzis aerophones,,reitboks discomposingly,,expandors,,monotasking galabia,,pertinents expedients witty,,chirographies crachach unsatisfactoriness swerveless,,flawed sepulchred thanksgiver scrawl skug,,perorate stringers gelatine flagstones,,chuses conceptualization surrejoined,,counterblasts rache,,numerative,,delirifacients methylthionine,,mantram dynamist atomised,,eternization percalines hryvnias pragmatizing,,reproachfulnesses telework nowts demoded revealer,,burnettize caryopteris subangular wirricows,,transvestites sinicized narcissus,,hikers meno,,degassing,,postcrises alikenesses,,sycophancy seroconverting insure,,yantras raphides cliftiest bosthoon,,zootherapy chlorides nationwide schlub yuri,,timeshares castanospermine backspaces reincite,,coactions cosignificative palafitte,,poofters subjunctions,,aquarian,,theralite revindicating,,cynosural permissibilities narcotising,,journeywork outkissed clarichords troutier,,myopias undiverting evacuations snarier superglue,,deaminise infirmaries teff hebephrenias,,brainboxes homonym lancelet,,lambitive stray,,inveigled,,acetabulums atenolol,,dekkos scarcer flensed,,abulias flaggers wammul boastfully,,galravitch happies interassociation multipara augmentations,,teratocarcinomata coopting didakai infrequently,,hairtails intricacy usuals,,pillorise outrating,,cataphoresis,,furnishings leglen,,goethite deflate butterburs,,phoneticising winiest hyposulphuric campshirts,,chainfalls swimmings roadblocked redone soliloquies,,broking mendaciousness parasitisms counterworld,,unravellings quarries passionately,,onomatopoesis repenting,,ramequin,,mopboard euphuistically,,volta sycophantized allantoides,,bors bouclees raisings sustaining,,diabolist sticks dole liltingly,,curial bisexualisms siderations hemolysed,,damnabilities unkenneling halters,,peripheral congaing,,diatomicity,,foolings repayments,,hereabouts vamosed him,,slanters moonrock porridgy monstruous,,heartwood bassoonist predispositions jargoon dominances,,timidest inalienable rewearing inevitably,,entreating retiary tranquillizing,,uniparental droogs,,allotropous,,forzati abiogenetic,,obduration exempted unifaces,,epilating calisaya dispiteously coggles,,vestmented flukily ignifying complished hiccupy municipalize,,pentagraphs parcels sutler excavates,,stardust miscited thankfulness,,fouter pertused,,overpacks,,guarishes hylotheism,,pi Fresh blood seeps through the line parting her skin and slowly colors her breast red. I begin to hyperventilate as my compulsion grows. The images won’t go away. Images of me driving the knife into her flesh continuously, fucking her body with the blade, making a mess of her. My head starts going crazy as my thoughts start to return. Shooting pain assaults my mind along with my thoughts. This is disgusting. Absolutely disgusting. How could I ever let myself think these things? But it’s unmistakable. The lust continues to linger through my veins. An ache in my muscles stems from the unreleased tension experienced by my entire body. Her Third Eye is drawing me closer.",
          "translation": null
        }
      ],
      "act_3": null
    }
  ]
}
```

</details>

### `GET /characters`

> https://ddlcapi.herokuapp.com/characters

Returns an array of objects with the data of each character.

<details>
  <summary>Response</summary>

```json
[
  {
    "name": "yuri",
    "age": 18,
    "born_date": "December 10th",
    "concept_height": "165 cm",
    "gender": "Female",
    "hair_color": "Dark Purple",
    "eye_color": "Light Purple",
    "filename": "yuri.chr",
    "appears": ["Act 1", "Act 2", "Act 4"],
    "voice_actor": null,
    "illustration": "https://ddlcapi.herokuapp.com/illustrations/yuri.png"
  },
  {
    "name": "monika",
    "age": 18,
    "born_date": "September 22nd",
    "concept_height": "160 cm",
    "gender": "Female",
    "hair_color": "Coral Brown",
    "eye_color": "Emerald Green",
    "filename": "monika.chr",
    "appears": ["Act 1", "Act 2", "Act 3", "Act 4"],
    "voice_actor": "Jillian Ashcraft",
    "illustration": "https://ddlcapi.herokuapp.com/illustrations/monika.png"
  },
  {
    "name": "natsuki",
    "age": 18,
    "born_date": "December 10th",
    "concept_height": "150 cm",
    "gender": "Female",
    "hair_color": "Pastel Pink",
    "eye_color": "Pink",
    "filename": "natsuki.chr",
    "appears": ["Act 1", "Act 2", "Act 4"],
    "voice_actor": null,
    "illustration": "https://ddlcapi.herokuapp.com/illustrations/natsuki.png"
  },
  {
    "name": "sayori",
    "age": 18,
    "born_date": "April 13",
    "concept_height": "157 cm",
    "gender": "Female",
    "hair_color": "Coral Pink",
    "eye_color": "Sky Blue",
    "filename": "sayori.chr",
    "appears": ["Act 1", "Act 4"],
    "voice_actor": null,
    "illustration": "https://ddlcapi.herokuapp.com/illustrations/sayori.png"
  }
]
```

</details>

### `GET /characters/{character}`

> https://ddlcapi.herokuapp.com/characters/yuri

Returns an object with the data of an specific character.

<details>
  <summary>Response</summary>

    ```json
    {
      "name": "yuri",
      "age": 18,
      "born_date": "December 10th",
      "concept_height": "165 cm",
      "gender": "Female",
      "hair_color": "Dark Purple",
      "eye_color": "Light Purple",
      "filename": "yuri.chr",
      "appears": ["Act 1", "Act 2", "Act 4"],
      "voice_actor": null,
      "illustration": "https://ddlcapi.herokuapp.com/illustrations/yuri.png"
    }
    ```

</details>

If you pass a character that doesn't exist you will receive:

> https://ddlcapi.herokuapp.com/characters/lol

```json
{ "detail": "Character \"lol\" not found." }
```

### `GET /poems`

Return an array of
[Character Poem Lists](https://github.com/UltiRequiem/ddlc_api/blob/main/ddlc/models.py#L33).

<details>
  <summary>Response</summary>

```json
[
  {
    "author": "natsuki",
    "act_1": [
      {
        "title": "Eagles Can Fly",
        "occasion": "This poem is shown on the second day.",
        "body": "Monkeys can climb\nCrickets can leap\nHorses can race\nOwls can seek\nCheetahs can run\nEagles can fly\nPeople can try\nBut that's about it.",
        "translation": null
      },
      {
        "title": "Amy Likes Spiders",
        "occasion": "This poem is shown on the third day.",
        "body": "You know what I heard about Amy?\nAmy likes spiders.\nIcky, wriggly, hairy, ugly spiders!\nThat's why I'm not friends with her.\n\nAmy has a cute singing voice.\nI heard her singing my favorite love song.\nEvery time she sang the chorus, my heart would pound to the rhythm of the words.\nBut she likes spiders.\nThat's why I'm not friends with her.\n\nOne time, I hurt my leg really bad.\nAmy helped me up and took me to the nurse.\nI tried not to let her touch me.\nShe likes spiders, so her hands are probably gross.\nThat's why I'm not friends with her.\n\nAmy has a lot of friends.\nI always see her talking to people.\nShe probably talks about spiders.\nWhat if her friends start to like spiders too?\nThat's why I'm not friends with her.\n\nIt doesn't matter if she has other hobbies.\nIt doesn't matter if she keeps it private.\nIt doesn't matter if it doesn't hurt anyone.\n\nIt's gross.\nShe's gross.\nThe world is better off without spider lovers.\n\nAnd I'm gonna tell everyone.",
        "translation": null
      },
      {
        "title": "Because You",
        "occasion": "This poem is shown on the fourth day, if the player made three poems that appeal to Natsuki.",
        "body": "Tomorrow will be brighter with me around\nBut when today is dim, I can only look down.\nMy looking is a little more forward\nBecause you look at me.\n\nWhen I want to say something, I say it with a shout!\nBut my truest feelings can never come out.\nMy words are a little less empty\nBecause you listen to me.\n\nWhen something is above me, I reach for the stars.\nBut when I feel small, I don't get very far.\nMy standing is a little bit taller\nBecause you sit with me.\n\nI believe in myself with all of my heart.\nBut what do I do when it's torn all apart?\nMy faith is a little bit stronger\nBecause you trusted me.\n\nMy pen always puts my feelings to the test.\nI'm not a good writer, but my best is my best.\nMy poems are a little bit dearer\nBecause you think of me.\n\nBecause you, because you, because you.",
        "translation": null
      },
      {
        "title": "I'll Be Your Beach",
        "occasion": "This poem is shown on the fourth day, if the player didn't make three poems that appeal to Natsuki.",
        "body": "Your mind is so full of troubles and fears\nThat diminished your wonder over the years\nBut today I have a special place\nA beach for us to go.\n\nA shore reaching beyond your sight\nA sea that sparkles with brilliant light\nThe walls in your mind will melt away\nBefore the sunny glow.\n\nI'll be the beach that washes your worries away\nI'll be the beach that you daydream about each day\nI'll be the beach that makes your heart leap\nIn a way you thought had left you long ago.\n\nLet's bury your heavy thoughts in a pile of sand\nBathe in sunbeams and hold my hand\nWash your insecurities in the salty sea\nAnd let me see you shine.\n\nLet's leave your memories in a footprint trail\nSet you free in my windy sail\nAnd remember the reasons you're wonderful\nWhen you press your lips to mine.\n\nI'll be the beach that washes your worries away\nI'll be the beach that you daydream about each day\nI'll be the beach that makes your heart leap\nIn a way you thought had left you long ago.\n\nBut if you let me by your side\nYour own beach, your own escape\nYou'll learn to love yourself again.",
        "translation": null
      }
    ],
    "act_2": [
      {
        "title": "T3BlbiBZb3VyIFRoaXJkIEV5ZQ==",
        "occasion": "This poem (written in Base64 code) is shown on the third day, if the player made two poems that appeal to Natsuki.",
        "body": "SSBjYW4gZmVlbCB0aGUgdGVuZGVybmVz\ncyBvZiBoZXIgc2tpbiB0aHJvdWdoIHRo\nZSBrbmlmZSwgYXMgaWYgaXQgd2VyZSBh\nbiBleHRlbnNpb24gb2YgbXkgc2Vuc2Ug\nb2YgdG91Y2guIE15IGJvZHkgbmVhcmx5\nIGNvbnZ1bHNlcy4gVGhlcmUncyBzb21l\ndGhpbmcgaW5jcmVkaWJseSBmYWludCwg\nZGVlcCBkb3duLCB0aGF0IHNjcmVhbXMg\ndG8gcmVzaXN0IHRoaXMgdW5jb250cm9s\nbGFibGUgcGxlYXN1cmUuIEJ1dCBJIGNh\nbiBhbHJlYWR5IHRlbGwgdGhhdCBJJ20g\nYmVpbmcgcHVzaGVkIG92ZXIgdGhlIGVk\nZ2UuIEkgY2FuJ3QuLi5JIGNhbid0IHN0\nb3AgbXlzZWxmLg==",
        "translation": {
          "title": "Open Your Third Eye",
          "body": "I can feel the tenderness of her skin through the knife, as if it were an extension of my sense of touch. My body nearly convulses. There's something incredibly faint, deep down, that screams to resist this uncontrollable pleasure. But I can already tell that I'm being pushed over the edge. I can't... I can't stop myself."
        }
      },
      {
        "title": "Natsuki's Request (No Title)",
        "occasion": "This poem is shown on the fourth day.",
        "body": "I don't know how else to bring this up. But there's been something\nI've been worried about. Yuri has been acting kind of strange lately.\nYou've only been here a few days, so you may not know what I mean. But\nshe's not normally like this. She's always been quiet and polite and\nattentive...things like that.\n\nOkay... This is really embarrassing, but I'm forcing myself to\nsuck it up. The truth is, I'm REALLY worried about her. But if I try\ntalking to her, she'll just get mad at me again. I don't know what to\ndo. I think you're the only person that she'll listen to. I don't know\nwhy. But please try to do something. Maybe you can convince her to talk\nto a therapist.\n\nI've always wanted to try being better friends with Yuri, and\nit really hurts me to see this happening. I know I'm going to hate\nmyself later for admitting that, but right now I don't care. I just feel\nso helpless. So please see if you can do something to help. I don't\nwant anything bad to happen to her. I'll make you cupcakes if I have to.\nJust please try to do something.\n\nAs for Monika... I don't know why, but she's been really dismissive about this. It's like she just wants us to ignore it. So I'm mad at her right now, and that's why I'm coming to you about this. DON'T LET HER KNOW I WROTE THIS!!!! Just pretend like I gave you a really good poem, okay? I'm counting on you. Thanks for reading.",
        "translation": null
      }
    ],
    "act_3": null
  },
  {
    "author": "sayori",
    "act_1": [
      {
        "title": "Dear Sunshine",
        "occasion": "This poem is shown on the second day.",
        "body": "The way you glow through my blinds in the morning\nIt makes me feel like you missed me.\nKissing my forehead to help me out of bed.\nMaking me rub the sleepy from my eyes.\n\nAre you asking me to come out and play?\nAre you trusting me to wish away a rainy day?\nI look above. The sky is blue.\nIt's a secret, but I trust you too.\n\nIf it wasn't for you, I could sleep forever.\nBut I'm not mad.\n\nI want breakfast.",
        "translation": null
      },
      {
        "title": "Bottles",
        "occasion": "This poem is shown on the third day.",
        "body": "I pop off my scalp like the lid of a cookie jar.\nIt's the secret place where I keep all my dreams.\nLittle balls of sunshine, all rubbing together like a bundle of kittens.\n\nI reach inside with my thumb and forefinger and pluck one out.\nIt's warm and tingly.\nBut there's no time to waste! I put it in a bottle to keep it safe.\nAnd I put the bottle on the shelf with all of the other bottles.\nHappy thoughts, happy thoughts, happy thoughts in bottles, all in a row.\n\nMy collection makes me lots of friends.\nEach bottle a starlight to make amends.\nSometimes my friend feels a certain way.\nDown comes a bottle to save the day.\n\nNight after night, more dreams.\nFriend after friend, more bottles.\nDeeper and deeper my fingers go.\nLike exploring a dark cave, discovering the secrets hiding in the nooks and crannies.\nDigging and digging.\nScraping and scraping.\n\nI blow dust off my bottle caps.\nIt doesn't feel like time elapsed.\nMy empty shelf could use some more.\nMy friends look through my locked front door.\n\nFinally, all done. I open up, and in come my friends.\nIn they come, in such a hurry. Do they want my bottles that much?\nI frantically pull them from the shelf, one after the other.\nHolding them out to each and every friend.\nEach and every bottle.\nBut every time I let one go, it shatters against the tile between my feet.\nHappy thoughts, happy thoughts, happy thoughts in shards, all over the floor.\n\nThey were supposed to be for my friends, my friends who aren't smiling.\nThey're all shouting, pleading. Something.\nBut all I hear is echo, echo, echo, echo, echo\nInside my head.",
        "translation": null
      },
      {
        "title": "%",
        "occasion": "This poem is shown on the festival day.",
        "body": "Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of\nGet.\nOut.\nOf.\nMy.\nHead.\n\n\nGet out of my head before I do what I know is best for you.\nGet out of my head before I listen to everything she said to me.\nGet out of my head before I show you how much I love you.\nGet out of my head before I finish writing this poem.\n\n\n\nBut a poem is never actually finished.\nIt just stops moving.",
        "translation": null
      }
    ],
    "act_2": null,
    "act_3": null
  },
  {
    "author": "yuri",
    "act_1": [
      {
        "title": "Ghost under the light",
        "occasion": "This poem is shown on the second day.",
        "body": "The tendrils of my hair illuminate beneath the amber glow.\nBathing.\nIt must be this one.\nThe last remaining streetlight to have withstood the test of time.\nThe last yet to be replaced by the sickening blue-green of the future.\nI bathe. Calm; breathing air of the present but living in the past.\nThe light flickers.\nI flicker back.",
        "translation": null
      },
      {
        "title": "The Raccoon",
        "occasion": "This poem is shown on the third day.",
        "body": "It happened in the dead of night while I was slicing bread for a guilty snack.\nMy attention was caught by the scuttering of a raccoon outside my window.\nThat was, I believe, the first time I noticed my strange tendencies as an unordinary\nhuman.\nI gave the raccoon a piece of bread, my subconscious well aware of the consequences.\nWell aware that a raccoon that is fed will always come back for more.\nThe enticing beauty of my cutting knife was the symptom.\nThe bread, my hungry curiosity.\nThe raccoon, an urge.\n\nThe moon increments its phase and reflects that much more light off of my cutting\nknife.\nThe very same light that glistens in the eyes of my raccoon friend.\nI slice the bread, fresh and soft. The raccoon becomes excited.\nor perhaps I'm merely projecting my emotions onto the newly-satisfied animal.\n\nThe raccoon has taken to following me.\nYou could say that we've gotten quite used to each other.\nThe raccoon becomes hungry more and more frequently, so my bread is always handy.\nEvery time I brandish my cutting knife the raccoon shows me its excitement.\nA rush of blood. Classic Pavlovian conditioning. I slice the bread.\n\nAnd I feed myself again.",
        "translation": null
      },
      {
        "title": "Ghost under the Light pt. 2",
        "occasion": "This poem is shown on the fourth day, if the player made three poems that appeal to Yuri.",
        "body": "The tendrils of my hair illuminate beneath the amber glow.\nBathing.\nIn the distance, a blue-green light flickers.\nA lone figure crosses its path– a silhouette obstructing the eerie glow.\nMy heart pounds. The silhouette grows. Closer Closer\nI open my umbrella, casting a shadow to shield me from visibility.\nBut I am too late.\nHe steps into the streetlight. I gasp and drop my umbrella.\nThe light flickers. My heart pounds. He raises his arm.\n\nTime stops.\n\nThe only indication of movement is the amber light flickering against his outstretched\narm.\nThe flickering light is in rhythm with the pounding of my heart.\nTeasing me for succumbing to this forbidden emotion.\nHave you ever heard of a ghost feeling warmth before?\nGiving up on understanding, I laugh.\nUnderstanding is overrated.\nI touch his hand. The flickering stops.\nGhosts are blue-green. My heart is amber.",
        "translation": null
      },
      {
        "title": "Beach",
        "occasion": "This poem is shown on the fourth day, if the player didn't make three poems that appeal to Yuri.",
        "body": "A marvel millions of years in the making.\nWhere the womb of Earth chaotically meets the surface.\nUnder a clear blue sky, an expanse of bliss -\nBut beneath gray rolling clouds, an endless enigma.\nThe easiest world to get lost in\nis one where everything can be found.\n\nOne can only build a sand castle where the sand is wet.\nBut where the sand is wet, the tide comes.\nWill it gently lick at your foundations until you give in?\nOr will a sudden wave send you crashing down in the blink of an eye?\nEither way the outcome is the same.\nYet we still build sand castles.\n\nI stand where the foam wraps around my ankles.\nWhere my toes squish into the sand.\nThe salty air is therapeutic.\nThe breeze is gentle, yet powerful.\nI sink my toes into the ultimate boundary line, tempted by the foamy tendrils.\nTurn back, and I abandon my peace to erode at the shore.\nDrift forward, and I return to Earth forevermore.",
        "translation": null
      }
    ],
    "act_2": [
      {
        "title": "Wheel",
        "occasion": "This poem is shown on the third day.",
        "body": "A rotating wheel. Turning an axle. Grinding. Bolthead. Linear gearbox. Falling sky. Seven holy stakes. A docked ship. A portal to another world. A thin rope tied to a thick rope. A torn harness. Parabolic gearbox. Expanding universe. Time controlled by slipping cogwheels. Existence of God. Swimming with open water in all directions. Drowning. A prayer written in blood. A prayer written in time-devouring snakes with human eyes. A thread connecting all living human eyes. A kaleidoscope of holy stakes. Exponential gearbox. A sky of exploding stars. God disproving the existence of God. A wheel rotating in six dimensions. Forty gears and a ticking clock. A clock that ticks one second for every rotation of the planet. A clock that ticks forty times every time it ticks every second time. A bolthead of holy stakes tied to the existence of a docked ship to another world. A kaleidoscope of blood written in clocks. A time-devouring prayer connecting a sky of forty gears and open human eyes in all directions. Breathing gearbox. Breathing bolthead. Breathing ship. Breathing portal. Breathing snakes. Breathing God. Breathing blood. Breathing holy stakes. Breathing human eyes. Breathing time. Breathing prayer. Breathing sky. Breathing wheel.",
        "translation": null
      },
      {
        "title": "mdpnfbo,jrfp",
        "occasion": "This poem is shown on the fourth day.",
        "body": "ed,,zinger suivante,,tels handknits finish,,cagefuls basinlike bag octopodan,,imbossing vaporettos rorid easygoingnesses nalorphines,,benzol respond washerwomen bristlecone,,parajournalism herringbone farnarkeled,,episodically cooties,,initiallers bimetallic,,leased hinters,,confidence teetotaller computerphobes,,pinnacle exotically overshades prothallia,,posterior gimmickry brassages bediapers countertrades,,haslet skiings sandglasses cannoli,,carven nis egomaniacal,,barminess gallivanted,,southeastward,,oophoron crumped,,tapued noncola colposcopical,,dolente trebbiano revealment,,outworked isotropous monosynaptic excisional moans,,enterocentesis jacuzzi preoccupations,,hippodrome outward googs,,tabbises undulators,,metathesizing,,sharia prepostor,,neuromast curmudgeons actability,,archaise spink reddening miscount,,madmen physostigmin statecraft neurocoeles bammed,,tenderest barguests crusados trust,,manshifts darzis aerophones,,reitboks discomposingly,,expandors,,monotasking galabia,,pertinents expedients witty,,chirographies crachach unsatisfactoriness swerveless,,flawed sepulchred thanksgiver scrawl skug,,perorate stringers gelatine flagstones,,chuses conceptualization surrejoined,,counterblasts rache,,numerative,,delirifacients methylthionine,,mantram dynamist atomised,,eternization percalines hryvnias pragmatizing,,reproachfulnesses telework nowts demoded revealer,,burnettize caryopteris subangular wirricows,,transvestites sinicized narcissus,,hikers meno,,degassing,,postcrises alikenesses,,sycophancy seroconverting insure,,yantras raphides cliftiest bosthoon,,zootherapy chlorides nationwide schlub yuri,,timeshares castanospermine backspaces reincite,,coactions cosignificative palafitte,,poofters subjunctions,,aquarian,,theralite revindicating,,cynosural permissibilities narcotising,,journeywork outkissed clarichords troutier,,myopias undiverting evacuations snarier superglue,,deaminise infirmaries teff hebephrenias,,brainboxes homonym lancelet,,lambitive stray,,inveigled,,acetabulums atenolol,,dekkos scarcer flensed,,abulias flaggers wammul boastfully,,galravitch happies interassociation multipara augmentations,,teratocarcinomata coopting didakai infrequently,,hairtails intricacy usuals,,pillorise outrating,,cataphoresis,,furnishings leglen,,goethite deflate butterburs,,phoneticising winiest hyposulphuric campshirts,,chainfalls swimmings roadblocked redone soliloquies,,broking mendaciousness parasitisms counterworld,,unravellings quarries passionately,,onomatopoesis repenting,,ramequin,,mopboard euphuistically,,volta sycophantized allantoides,,bors bouclees raisings sustaining,,diabolist sticks dole liltingly,,curial bisexualisms siderations hemolysed,,damnabilities unkenneling halters,,peripheral congaing,,diatomicity,,foolings repayments,,hereabouts vamosed him,,slanters moonrock porridgy monstruous,,heartwood bassoonist predispositions jargoon dominances,,timidest inalienable rewearing inevitably,,entreating retiary tranquillizing,,uniparental droogs,,allotropous,,forzati abiogenetic,,obduration exempted unifaces,,epilating calisaya dispiteously coggles,,vestmented flukily ignifying complished hiccupy municipalize,,pentagraphs parcels sutler excavates,,stardust miscited thankfulness,,fouter pertused,,overpacks,,guarishes hylotheism,,pi Fresh blood seeps through the line parting her skin and slowly colors her breast red. I begin to hyperventilate as my compulsion grows. The images won’t go away. Images of me driving the knife into her flesh continuously, fucking her body with the blade, making a mess of her. My head starts going crazy as my thoughts start to return. Shooting pain assaults my mind along with my thoughts. This is disgusting. Absolutely disgusting. How could I ever let myself think these things? But it’s unmistakable. The lust continues to linger through my veins. An ache in my muscles stems from the unreleased tension experienced by my entire body. Her Third Eye is drawing me closer.",
        "translation": null
      }
    ],
    "act_3": null
  }
]
```

</details>

### `GET /poems/{author}`

> https://ddlcapi.herokuapp.com/poems/natsuki

Return a
[Character Poem List](https://github.com/UltiRequiem/ddlc_api/blob/main/ddlc/models.py#L33).

<details>
  <summary>Response</summary>

```json
{
  "author": "natsuki",
  "act_1": [
    {
      "title": "Eagles Can Fly",
      "occasion": "This poem is shown on the second day.",
      "body": "Monkeys can climb\nCrickets can leap\nHorses can race\nOwls can seek\nCheetahs can run\nEagles can fly\nPeople can try\nBut that's about it.",
      "translation": null
    },
    {
      "title": "Amy Likes Spiders",
      "occasion": "This poem is shown on the third day.",
      "body": "You know what I heard about Amy?\nAmy likes spiders.\nIcky, wriggly, hairy, ugly spiders!\nThat's why I'm not friends with her.\n\nAmy has a cute singing voice.\nI heard her singing my favorite love song.\nEvery time she sang the chorus, my heart would pound to the rhythm of the words.\nBut she likes spiders.\nThat's why I'm not friends with her.\n\nOne time, I hurt my leg really bad.\nAmy helped me up and took me to the nurse.\nI tried not to let her touch me.\nShe likes spiders, so her hands are probably gross.\nThat's why I'm not friends with her.\n\nAmy has a lot of friends.\nI always see her talking to people.\nShe probably talks about spiders.\nWhat if her friends start to like spiders too?\nThat's why I'm not friends with her.\n\nIt doesn't matter if she has other hobbies.\nIt doesn't matter if she keeps it private.\nIt doesn't matter if it doesn't hurt anyone.\n\nIt's gross.\nShe's gross.\nThe world is better off without spider lovers.\n\nAnd I'm gonna tell everyone.",
      "translation": null
    },
    {
      "title": "Because You",
      "occasion": "This poem is shown on the fourth day, if the player made three poems that appeal to Natsuki.",
      "body": "Tomorrow will be brighter with me around\nBut when today is dim, I can only look down.\nMy looking is a little more forward\nBecause you look at me.\n\nWhen I want to say something, I say it with a shout!\nBut my truest feelings can never come out.\nMy words are a little less empty\nBecause you listen to me.\n\nWhen something is above me, I reach for the stars.\nBut when I feel small, I don't get very far.\nMy standing is a little bit taller\nBecause you sit with me.\n\nI believe in myself with all of my heart.\nBut what do I do when it's torn all apart?\nMy faith is a little bit stronger\nBecause you trusted me.\n\nMy pen always puts my feelings to the test.\nI'm not a good writer, but my best is my best.\nMy poems are a little bit dearer\nBecause you think of me.\n\nBecause you, because you, because you.",
      "translation": null
    },
    {
      "title": "I'll Be Your Beach",
      "occasion": "This poem is shown on the fourth day, if the player didn't make three poems that appeal to Natsuki.",
      "body": "Your mind is so full of troubles and fears\nThat diminished your wonder over the years\nBut today I have a special place\nA beach for us to go.\n\nA shore reaching beyond your sight\nA sea that sparkles with brilliant light\nThe walls in your mind will melt away\nBefore the sunny glow.\n\nI'll be the beach that washes your worries away\nI'll be the beach that you daydream about each day\nI'll be the beach that makes your heart leap\nIn a way you thought had left you long ago.\n\nLet's bury your heavy thoughts in a pile of sand\nBathe in sunbeams and hold my hand\nWash your insecurities in the salty sea\nAnd let me see you shine.\n\nLet's leave your memories in a footprint trail\nSet you free in my windy sail\nAnd remember the reasons you're wonderful\nWhen you press your lips to mine.\n\nI'll be the beach that washes your worries away\nI'll be the beach that you daydream about each day\nI'll be the beach that makes your heart leap\nIn a way you thought had left you long ago.\n\nBut if you let me by your side\nYour own beach, your own escape\nYou'll learn to love yourself again.",
      "translation": null
    }
  ],
  "act_2": [
    {
      "title": "T3BlbiBZb3VyIFRoaXJkIEV5ZQ==",
      "occasion": "This poem (written in Base64 code) is shown on the third day, if the player made two poems that appeal to Natsuki.",
      "body": "SSBjYW4gZmVlbCB0aGUgdGVuZGVybmVz\ncyBvZiBoZXIgc2tpbiB0aHJvdWdoIHRo\nZSBrbmlmZSwgYXMgaWYgaXQgd2VyZSBh\nbiBleHRlbnNpb24gb2YgbXkgc2Vuc2Ug\nb2YgdG91Y2guIE15IGJvZHkgbmVhcmx5\nIGNvbnZ1bHNlcy4gVGhlcmUncyBzb21l\ndGhpbmcgaW5jcmVkaWJseSBmYWludCwg\nZGVlcCBkb3duLCB0aGF0IHNjcmVhbXMg\ndG8gcmVzaXN0IHRoaXMgdW5jb250cm9s\nbGFibGUgcGxlYXN1cmUuIEJ1dCBJIGNh\nbiBhbHJlYWR5IHRlbGwgdGhhdCBJJ20g\nYmVpbmcgcHVzaGVkIG92ZXIgdGhlIGVk\nZ2UuIEkgY2FuJ3QuLi5JIGNhbid0IHN0\nb3AgbXlzZWxmLg==",
      "translation": {
        "title": "Open Your Third Eye",
        "body": "I can feel the tenderness of her skin through the knife, as if it were an extension of my sense of touch. My body nearly convulses. There's something incredibly faint, deep down, that screams to resist this uncontrollable pleasure. But I can already tell that I'm being pushed over the edge. I can't... I can't stop myself."
      }
    },
    {
      "title": "Natsuki's Request (No Title)",
      "occasion": "This poem is shown on the fourth day.",
      "body": "I don't know how else to bring this up. But there's been something\nI've been worried about. Yuri has been acting kind of strange lately.\nYou've only been here a few days, so you may not know what I mean. But\nshe's not normally like this. She's always been quiet and polite and\nattentive...things like that.\n\nOkay... This is really embarrassing, but I'm forcing myself to\nsuck it up. The truth is, I'm REALLY worried about her. But if I try\ntalking to her, she'll just get mad at me again. I don't know what to\ndo. I think you're the only person that she'll listen to. I don't know\nwhy. But please try to do something. Maybe you can convince her to talk\nto a therapist.\n\nI've always wanted to try being better friends with Yuri, and\nit really hurts me to see this happening. I know I'm going to hate\nmyself later for admitting that, but right now I don't care. I just feel\nso helpless. So please see if you can do something to help. I don't\nwant anything bad to happen to her. I'll make you cupcakes if I have to.\nJust please try to do something.\n\nAs for Monika... I don't know why, but she's been really dismissive about this. It's like she just wants us to ignore it. So I'm mad at her right now, and that's why I'm coming to you about this. DON'T LET HER KNOW I WROTE THIS!!!! Just pretend like I gave you a really good poem, okay? I'm counting on you. Thanks for reading.",
      "translation": null
    }
  ],
  "act_3": null
}
```

</details>

If you pass a character that doesn't exist you will receive:

> https://ddlcapi.herokuapp.com/poems/lol

```json
{ "detail": "Character \"Lol\" not found." }
```

### `GET /illustrations`

> https://ddlcapi.herokuapp.com/illustrations

An object, key is the character name and the value is a link with the
illustration.

<details>
  <summary>response</summary>

```json
{
  "yuri": "https://ddlcapi.herokuapp.com/illustrations/yuri.png",
  "natsuki": "https://ddlcapi.herokuapp.com/illustrations/natsuki.png",
  "sayori": "https://ddlcapi.herokuapp.com/illustrations/sayori.png",
  "monika": "https://ddlcapi.herokuapp.com/illustrations/monika.png"
}
```

</details>

### `GET /illustrations/{character}.png`

> https://ddlcapi.herokuapp.com/illustrations/natsuki.png

The illustration of `{character}`.

<details>
  <summary>Response</summary>

![Natsuki Image](https://ddlcapi.herokuapp.com/illustrations/natsuki.png)

</details>

## Development / Production

1. Install [Poetry](https://python-poetry.org)

2. Create a virtual environment

```sh
poetry shell
```

3. Install the dependencies

```sh
poetry install
```

4. Start the process

- Production

```sh
uvicorn ddlc:app
```

- Development

```sh
ENV=dev uvicorn ddlc:app --reload
```

## License

This project is licensed under the [MIT License](./license).

[Team Salvato Intellectual Property Guidelines](http://teamsalvato.com/ip-guidelines).
