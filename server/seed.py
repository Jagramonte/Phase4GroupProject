#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import Genre, User, Movie

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        u1 = User('Jojo')

        g1 = Genre('Horror')
        g2 = Genre('Comedy')
        g3 = Genre('Romance')
        g4 = Genre('Action')
        g5 = Genre('Scifi')

        m1 = Movie(4,1, 'Die Hard', 'NYPD officer John McClane battles terrorists in a Los Angeles skyscraper on Christmas Eve, creating a high-octane, iconic action thriller.')
        m2 = Movie(4,1, 'Iron Monkey', 'A masked martial artist fights corruption in a small town, delivering breathtaking kung fu sequences and choreography.')
        m3 = Movie(4,1, 'Lone Survivor', 'Based on a true story, a Navy SEAL team faces an intense and harrowing battle in Afghanistan, testing their courage and resilience.')
        m4 = Movie(4,1, 'Top Gun', 'Maverick, a talented fighter pilot, competes for the top spot in an elite training school, blending adrenaline-pumping aerial sequences with a tale of rivalry and redemption.')
        m5 = Movie(4,1, '13 Hours', 'A gripping account of the Benghazi attack unfolds as a group of security contractors faces a desperate fight for survival against overwhelming odds.')
        m6 = Movie(4,1, 'Batman Forever', 'Batman faces Two-Face and the Riddler in this neon-soaked installment, exploring the darker side of Batman.')
        m7 = Movie(4,1, 'Point Break', 'An FBI agent goes undercover to infiltrate a group of thrill-seeking bank robbers, leading to a dangerous game of cat and mouse.')
        m8 = Movie(4,1, 'Kingsman', ' A stylish and witty spy film follows a young recruit as he trains to become a member of an elite, unconventional secret service.')
        m9 = Movie(4,1, 'Mission Impossible', 'Ethan Hunt, a skilled operative, embarks on daring missions filled with suspense, intricate plots, and jaw-dropping stunts.')
        m10 = Movie(4,1, 'Heat','A gripping crime saga unfolds as a master thief and a determined detective engage in a high-stakes cat-and-mouse game in Los Angeles.')
        m11 = Movie(4,1,'The Town', 'A group of bank robbers faces the challenges of crime and redemption in the tight-knit community of Charlestown, Boston')
        m12 = Movie(4,1,'Tenet', 'A mind-bending thriller explores time inversion as a protagonist tries to prevent a global catastrophe.')
        m13 = Movie(4,1, 'Taken', 'A former CIA operative with a particular set of skills embarks on a relentless quest to rescue his kidnapped daughter in this action-packed thriller.')
        m14 = Movie(4,1, 'Bad Boys', 'Will Smith and Martin Lawrence star as Miami detectives in this explosive and humorous buddy-cop film.')
        m15 = Movie(4,1, 'John Wick', 'Keanu Reeves delivers a relentless and stylish performance as an ex-hitman seeking vengeance for the death of his beloved dog.')
        m16 = Movie(2,1, 'Tropic Thunder', 'A group of self-absorbed actors inadvertently find themselves in a real-life war zone, leading to hilarious and chaotic misadventures.')
        m17 = Movie(2,1, 'Big Daddy', 'Adam Sandler plays an irresponsible bachelor who learns about maturity and responsibility when he unexpectedly becomes the legal guardian of a young boy.')
        m18 = Movie(2,1, 'Superbad', 'A wild and raunchy coming-of-age comedy follows two high school friends on a mission to buy alcohol for a party and impress their crushes.')
        m19 = Movie(2,1, 'Wedding Crashers', 'Two friends make a hobby out of crashing weddings to meet women, but their scheme takes an unexpected turn when they encounter love and true commitment.')
        m20 = Movie(2,1, 'This is The End', 'A group of celebrities face the apocalypse at a house party, leading to absurd and hysterical situations in this meta-comedy.')
        m21 = Movie(2,1, 'The Hangover', 'A bachelor party in Las Vegas goes hilariously awry as a group of friends wakes up with no memory of the previous night and a missing groom.')
        m22 = Movie(2,1, 'Harold & Kumar Go To White Castle', 'Two stoners embark on an epic journey for White Castle burgers, encountering bizarre characters and outrageous obstacles along the way.')
        m23 = Movie(2,1, 'Borat', 'A satirical mockumentary follows the misadventures of the fictional Kazakh journalist as he travels across America, exposing cultural prejudices.')
        m24 = Movie(2,1, 'Zoolander', 'A dim-witted male model becomes unwittingly involved in a sinister plot to assassinate the Prime Minister of Malaysia in this hilarious fashion industry satire.')
        m25 = Movie(2,1, 'Forgetting Sarah Marshall', 'A heartbroken man attempts to move on from a recent breakup, only to find himself awkwardly vacationing at the same resort as his ex and her new boyfriend.')
        m26 = Movie(2,1, 'The 40 Year Old Virgin', 'Steve Carell stars as a middle-aged man on a quest to lose his virginity, leading to a series of comedic and endearing escapades.')
        m27 = Movie(2,1, 'Dodgeball', 'In a bid to save their gym from bankruptcy, a group of misfits enters a high-stakes dodgeball tournament against a ruthless and comically villainous competitor.')
        m28 = Movie(2,1, 'Step Brothers', 'Two middle-aged men become unlikely stepbrothers, leading to a series of outrageous and absurdly funny clashes as they refuse to grow up.')
        m29 = Movie(2,1, 'The Longest Yard', 'A former football player leads a team of inmates in a football game against the prison guards, blending humor with sports in this classic comedy.')
        m30 = Movie(3,1, 'The Notebook', 'A timeless love story unfolds as Noah and Allie navigate the challenges of societal expectations and personal sacrifices.')
        m31 = Movie(3,1, 'P.S. I Love You', 'After her husband\'s untimely death, Holly discovers a series of heartfelt letters that guide her on a journey of self-discovery and healing.')
        m32 = Movie(3,1, 'Ghost', 'Love transcends mortality when a man communicates with his grieving girlfriend through a psychic medium after his murder.')
        m33 = Movie(3,1, 'No Strings Attached', 'Friends attempt to keep their relationship strictly physical, but emotions complicate their arrangement in this romantic comedy.')
        m34 = Movie(3,1, 'About Time', 'Tim discovers the extraordinary gift of time travel and uses it to find love and create meaningful moments in this heartwarming and comedic tale.')
        m35 = Movie(3,1, 'Inception', 'A mind-bending heist film explores dreams within dreams as Dom Cobb delves into the origins of ideas and the power of the subconscious')
        m36 = Movie(3,1, 'Me Before You', 'A young woman\'s life takes an unexpected turn when she becomes a caregiver for a quadriplegic man, leading to an emotional and transformative journey.')
        m37 = Movie(3,1, 'Definitely Maybe', 'Aspiring politician Will recounts his romantic history to his daughter, sparking a quest for her to uncover the identity of her mother.')
        m38 = Movie(3,1, 'A Star Is Born', 'The tumultuous love story of a seasoned musician and a rising star explores the highs and lows of fame, addiction, and the music industry.')
        m39 = Movie(3,1, 'The Time Travelor\'s Wife', 'A man with a genetic disorder involuntarily travels through time, creating challenges and complexities in his marriage.')
        m40 = Movie(3,1, 'Pride & Prejudice', 'Jane Austen\'s classic tale follows the complex courtship between Elizabeth Bennet and Mr. Darcy in 19th-century England.')
        m41 = Movie(3,1, 'The Lovers', 'A married couple reignites their passion when both discover they are having affairs in this provocative exploration of love and desire.')
        m42 = Movie(3,1, '50 First Dates', 'A man falls for a woman with short-term memory loss, leading him to win her heart every day in this charming romantic comedy.')
        m43 = Movie(3,1, 'Pearl Harbor', 'Love and friendship are tested amidst the backdrop of the infamous attack on Pearl Harbor during World War II.')
        m44 = Movie(3,1, 'Titanic', 'The epic romance between Jack and Rose unfolds against the tragic sinking of the Titanic, testing the limits of love and survival.')
        m45 = Movie(2,1, 'The Water Boy', 'A socially awkward water boy with a hidden talent for football becomes an unexpected sports sensation, bringing both laughs and heart to the field.')
        m46 = Movie(5,1, 'The Fifth Element', 'A visually stunning and action-packed sci-fi adventure that follows a cab driver and a mysterious woman as they race against time to save the world from an ancient evil force.')
        m47 = Movie(5,1, 'Jurassic Park', 'A thrilling Steven Spielberg classic that brings dinosaurs back to life through groundbreaking special effects, as a group of people must survive the chaos unleashed when an amusement park\'s cloned dinosaurs run amok.')
        m48 = Movie(5,1, 'Men In Black', 'A combination of humor and science fiction in a story where two secret agents, played by Will Smith and Tommy Lee Jones, protect Earth from extraterrestrial threats and ensure the public remains oblivious to the existence of aliens.')
        m49 = Movie(5,1, 'The Matrix', 'A mind-bending story about a computer hacker, Neo, who discovers the truth about reality and joins a rebellion against intelligent machines controlling humanity.')
        m50 = Movie(5,1, 'Interstellar', 'A visually stunning space epic directed by Christopher Nolan, exploring the journey of astronauts who travel through a wormhole in search of a new habitable planet for humanity.')
        m51 = Movie(5,1, 'Edge of Tomorrow', 'A soldier relives the same day of a deadly alien invasion repeatedly, gaining skills to turn the tide of the war.')
        m52 = Movie(5,1, 'Alien', 'Sigourney Weaver as Ellen Ripley, the lone survivor of a deep-space mining crew terrorized by a deadly extraterrestrial creature.')
        m53 = Movie(5,1, 'Predator', 'An intense action film where Arnold Schwarzenegger leads a team of commandos facing a deadly extraterrestrial hunter in the jungle.')
        m54 = Movie(5,1, 'Planet of The Apes', 'A dystopian future where intelligent apes rule and humans are subjugated, offering social commentary on humanity and power dynamics.')
        m55 = Movie(5,1, 'Inception', 'A mind-bending thriller directed by Christopher Nolan, where a skilled thief enters people\'s dreams to steal their secrets, pushing the boundaries of reality and perception.')
        m56 = Movie(5,1, 'Avatar', 'The visually groundbreaking epic set on the alien moon Pandora, following a paraplegic marine who becomes involved in a conflict between humans and the indigenous Na\'vi.')
        m57 = Movie(5,1, 'Terminator', 'A sci-fi classic that introduces the iconic character of the Terminator, a relentless cyborg sent from the future to assassinate Sarah Connor, whose son will play a crucial role in the war against machines.')
        m58 = Movie(5,1, 'Transformers', 'A Michael Bay-directed action extravaganza where giant robots, the Autobots and Decepticons, bring their war to Earth.')
        m59 = Movie(5,1, 'Star Wars', 'A space opera saga created by George Lucas, featuring iconic characters like Luke Skywalker and Darth Vader, set in a galaxy far, far away, filled with the Force, Jedi, and epic battles between the Rebel Alliance and the Galactic Empire.')
        m60 = Movie(5,1, 'The Time Machine', 'The classic adaptation of H.G. Wells\' novel, following a Victorian-era inventor who creates a machine that allows him to travel through time, witnessing the future evolution of humanity.')
        m61 = Movie(1,1, 'IT', 'A malevolent clown named Pennywise terrorizes a group of children in the small town of Derry.')
        m62 = Movie(1,1, 'As Above So Below', 'A nightmarish journey through the catacombs beneath Paris as a team of explorers faces supernatural terrors.')
        m63 = Movie(1,1, 'The Exorcist', 'A classic horror film directed by William Friedkin, centered around a young girl possessed by a demonic force, leading to a battle between good and evil.')
        m64 = Movie(1,1, 'The Nightmare on Elm Street', 'Freddy Krueger, a vengeful spirit who haunts the dreams of teenagers, with deadly consequences in the real world.')
        m65 = Movie(1,1,'Saw', 'a psychological horror film that follows a twisted game master, Jigsaw, who tests people\'s will to survive through gruesome and elaborate traps.')
        m66 = Movie(1,1, 'The Nun', 'Part of The Conjuring Universe, exploring the demonic origins of the haunting nun character as investigators confront evil in a Romanian abbey.')
        m67 = Movie(1,1, 'Insidious', 'A family seeks to rescue their comatose son from malevolent entities haunting the astral plane.')
        m68 = Movie(1,1, 'The Conjuring', 'Paranormal investigators Ed and Lorraine Warren confront a dark presence in a farmhouse.')
        m69 = Movie(1,1, 'The Shining', 'Directed by Stanley Kubrick, is a psychological horror masterpiece that follows a family\'s descent into madness while isolated in a haunted hotel.')
        m70 = Movie(1,1, 'Lights Out', 'A horror film where a family is terrorized by a malevolent entity that can only manifest in the darkness.')
        m71 = Movie(1,1, 'Child\'s Play', 'Chucky, possessed by a serial killer\'s soul, goes on a murderous rampage.')
        m72 = Movie(1,1, 'Misery', 'A psychological thriller based on Stephen King\'s novel, depicting a novelist held captive by an obsessed fan after a car accident.')
        m73 = Movie(1,1, 'Scream', 'A self-aware slasher film that satirizes horror tropes while delivering suspense and thrills as a masked killer targets a group of high school students.')
        m74 = Movie(1,1, 'Get Out', 'A social thriller that explores racial tension and horror when a young African American man visits his white girlfriend\'s family estate.')
        m75 = Movie(1,1, 'Hereditary', 'A chilling and atmospheric horror film that explores a family\'s dark and supernatural history, unraveling terrifying secrets after the death of their secretive grandmother.')

        db.session.add(u1)

        db.session.add_all([g1, g2, g3, g4, g5])

        db.session.add_all([m1, m2, m3, m4, m5, m6, m7, m8, m9, m10,m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23, m24, m25, m26, m27, m28, m29, m30,m31, m32, m33, m34, m35, m36, m37, m38, m39, m40, m41, m42, m43, m44, m45, m46, m47, m48, m49, m50, m51, m52, m53, m54, m55, m56, m57, m58, m59, m60, m61, m62, m63, m64, m65, m66, m67, m68, m69, m70,m71, m72, m73, m74, m75])
        db.session.commit()
        print("Seed completed.")