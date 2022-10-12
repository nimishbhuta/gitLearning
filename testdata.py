renewal_se_customers1 = [
    # CustomerID, Name, PIN, AgreementChoice. premiseId
    ("1000449399", "Lena Karlsson", "5796", "1", "RSK735999100002613263"),  # Discounts, 3ÅR_BR, rtc, asserts
    ("1000735014", "Koncy Carlsson", "8523", "1", "DAD735999100053227983")  # No discounts, NORM, rtc, asserts
    ]

renewal_se_sme_customers = [
    # CustomerID, Name, PIN, AgreementChoice, premiseId
    ("1000250385", "a", "6197", "1", "OGO735999114000009065"),
    ("1000023358", "b", "7546", "1", "KAB735999100056661975"), 
    ("1000524184", "rjan", "0912", "1", "AJB735999100056550590"), 
    ("1000373215", "rjan", "0413", "1", "GDB735999100056296795"), 
    ("2000343678", "rjan", "3392", "1", "DAD735999100005220116"),
    ("2000366748", "rjan", "5470", "1", "ARD735999100000609688")    
    ]

new_customer_se_customers = [
    # Ssn, FirstName, LastName, PhoneNr, AgreementChoice, Address, ZIP, POD id, kWh
    ("740404-0995", "TestkundA", "TestkundE", "0730341500", "2", "Kyrkbacken 21", "16962", "100056658883", "6000"),
    ("740404-0995", "TestkundB", "TestkundE", "0730341500", "1", "Kyrkbacken 22", "16962", "100056658883", "custom_100")
    ]

renewal_fi_customers = [
    # customerNumber, Name, agreementNumber
    ("7888999", "Testi Testinen", "9999123456"),  # Prod and sys
    ("8888999", "Hakki Halinen", "9998123456"),  
    ("2199999", "Hannu Halinen", "1198345678")     # ?
    ]

view_contract_se_customers = [
    # CustomerID, Name, PIN
    ("1000334765", "X", "0546"),    # 3ÅR_BR, discounts
    ("1000683182", "X", "9112"),    # 3ÅR, no discounts
    ("1000512630", "X", "1002"),    # Spot
    ('2001003819', "X", '1914'),    # Anvisningsavtal
    ('1000149454', "X", '0388'),    # Heat, fixed, no hotwater
    ('1000415730', "X", '0177'),    # Heat, fixed, hotwater
    ('1000679122', "X", '4237'),    # Heat, spot, no hotwater
    ('1000550351', "X", '4588')     # Heat, spot, hotwater
    ]

mco_se_customers = [
    # CustomerID, Name, PIN, ZIP, AgreementChoice, Address, POD id, kWh
    ("1000512630", "Testerson", "1002", "16962", "1", "Testgatan 999", "100056658883", "3000"),
    ("1000512630", "T Testerson", "1002", "16962", "2", "Testgatan 999", "unknown", "25000"),
    ("1000512630", "Testerson", "1002", "16962", "2", "Testv 000", "100056658883", "custom_99999"),
    ("1000512630", "Testerson", "1002", "16962", "3", "Testv 0", "100056658883", "custom_99")
    ]

sme_new_move_customer = [
    # CustomerID, Name, PIN, ZIP, AgreementChoice, Address, POD id, kWh
    ("1000512630", "Testerson", "1002", "16962", "1", "Testgatan 999", "100056658883", "3000"),
    ("1000512630", "T Testerson", "1002", "16962", "2", "Testgatan 999", "unknown", "25000"),
    ("1000512630", "Testerson", "1002", "16962", "2", "Testv 000", "100056658883", "custom_99999"),
    ("1000512630", "Testerson", "1002", "16962", "3", "Testv 0", "100056658883", "custom_99")
    ]
 