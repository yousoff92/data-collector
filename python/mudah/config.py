from enum import Enum

class General(Enum):
  MUDAH_URL = "http://www.mudah.my"
  CHROME_PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

  # If set to 10, it will retrieve 10 pages with latest properties. Set to -1 to get all available properties.  
  PAGE_THRESHOLD = 3

class Region(Enum):
  KUALA_LUMPUR = "/Kuala-Lumpur"
  SELANGOR = "/Selangor"
  NEIGHBOURING = "/Neighbouring-9"
  ENTIRE_MALAYSIA = "/Malaysia"
  JOHOR =  "/Johor"
  KEDAH =  "/Kedah"
  KELANTAN = "/Kelantan"
  LABUAN = "/Labuan"
  MELAKA = "/Melaka"
  NEGERI_SEMBILAN = "/Negeri-Sembilan"
  PAHANG =  "/Pahang"
  PENANG = "/Penang"
  PERAK = "/Perak"
  PERLIS = "/Perlis"
  PUTRAJAYA = "/Putrajaya"
  SABAH = "/Sabah"
  SARAWAK = "/Sarawak"
  TERENGGANU = "/Terengganu"

class PropertyCategory(Enum):
  APARTMENT = "/Apartments-for-rent-2020"
  HOUSE = "/Houses-for-rent-2040"
  COMMERCIAL = "/Commercial-Properties-for-rent-2060"
  LANDED = "/Land-for-rent-2080"
  ROOM = "/Rooms-for-rent-2100"

class SupportedPropertyRegionArea:
    areas = [Region.KUALA_LUMPUR, Region.SELANGOR]

class PropertyArea(Enum):
  SGR_ALAM_IMPIAN = 611
  SGR_AMAN_PERDANA = 614
  SGR_AMPANG = 268
  SGR_AMBANG_BOTANIC = 601
  SGR_ARA_DAMANSARA = 269
  SGR_BALAKONG = 270
  SGR_BANDAR_BOTANIC = 612
  SGR_BANDAR_BUKIT_RAJA = 271
  SGR_BANDAR_BUKIT_TINGGI = 602
  SGR_BANDAR_KINRARA = 272
  SGR_BANDAR_PUTERI_KLANG = 615
  SGR_BANDAR_PUTERI_PUCHONG = 273
  SGR_BANDAR_SAUJANA_PUTRA = 613
  SGR_BANDAR_SUNGAI_LONG = 616
  SGR_BANDAR_SUNWAY = 274
  SGR_BANDAR_UTAMA = 275
  SGR_BANGI = 276
  SGR_BANTING = 277
  SGR_BATANG_BERJUNTAI = 278
  SGR_BATANG_KALI = 279
  SGR_BATU_ARANG = 280
  SGR_BATU_CAVES = 281
  SGR_BERANANG = 282
  SGR_BUKIT_ANTARABANGSA = 597
  SGR_BUKIT_BERUNTUNG = 640
  SGR_BUKIT_JELUTONG = 603
  SGR_BUKIT_RAHMAN_PUTRA = 609
  SGR_BUKIT_ROTAN = 283
  SGR_BUKIT_SUBANG = 604
  SGR_CHERAS = 284
  SGR_COUNTRY_HEIGHTS = 285
  SGR_CYBERJAYA = 286
  SGR_DAMANSARA_DAMAI = 287
  SGR_DAMANSARA_INTAN = 288
  SGR_DAMANSARA_JAYA = 289
  SGR_DAMANSARA_KIM = 290
  SGR_DAMANSARA_PERDANA = 291
  SGR_DAMANSARA_UTAMA = 292
  SGR_DENAI_ALAM = 610
  SGR_DENGKIL = 293
  SGR_GLENMARIE = 294
  SGR_GOMBAK = 598
  SGR_HULU_LANGAT = 295
  SGR_HULU_SELANGOR = 296
  SGR_JENJAROM = 297
  SGR_KAJANG = 298
  SGR_KAPAR = 299
  SGR_KAYU_ARA = 300
  SGR_KELANA_JAYA = 301
  SGR_KERLING = 302
  SGR_KLANG = 303
  SGR_KOTA_DAMANSARA = 304
  SGR_KOTA_EMERALD = 605
  SGR_KOTA_KEMUNING = 305
  SGR_KUALA_KUBU_BARU = 306
  SGR_KUALA_LANGAT = 307
  SGR_KUALA_SELANGOR = 308
  SGR_KUANG = 309
  SGR_MUTIARA_DAMANSARA = 310
  SGR_PETALING_JAYA = 312
  SGR_PORT_KLANG = 313
  SGR_PUCHONG = 314
  SGR_PUCHONG_SOUTH = 617
  SGR_PULAU_INDAH = 315
  SGR_PULAU_CAREY = 316
  SGR_PULAU_KETAM = 317
  SGR_PUNCAK_ALAM = 643
  SGR_PUNCAK_JALIL = 318
  SGR_PUTRA_HEIGHTS = 319
  SGR_RASA = 321
  SGR_RAWANG = 322
  SGR_SABAK_BERNAM = 323
  SGR_SALAK_TINGGI = 350
  SGR_SAUJANA = 606
  SGR_SAUJANA_UTAMA = 620
  SGR_SEKINCHAN = 324
  SGR_SELAYANG = 325
  SGR_SEMENYIH = 326
  SGR_SEPANG = 327
  SGR_SERDANG = 328
  SGR_SERENDAH = 329
  SGR_SERI_KEMBANGAN = 330
  SGR_SETIA_ALAM = 331
  SGR_SETIA_ECO_PARK = 332
  SGR_SHAH_ALAM = 333
  SGR_SIERRAMAS = 334
  SGR_SS2 = 336
  SGR_SUBANG_BESTARI = 618
  SGR_SUBANG_HEIGHTS = 607
  SGR_SUBANG_JAYA = 337
  SGR_SUBANG_PERDANA = 647
  SGR_SUNGAI_AYER_TAWAR = 338
  SGR_SUNGAI_BESAR = 339
  SGR_SUNGAI_BULOH = 340
  SGR_SUNGAI_PELEK = 341
  SGR_TAMAN_TTDI_JAYA = 608
  SGR_TANJONG_KARANG = 342
  SGR_TANJONG_SEPAT = 343
  SGR_TELOK_PANGLIMA_GARANG = 344
  SGR_TROPICANA = 345
  SGR_ULU_KLANG = 346
  SGR_USJ = 347
  SGR_USJ_HEIGHTS = 619
  SGR_VALENCIA = 348
  SGR_OTHERS = 349
  KL_AMPANG_HILIR = 628
  KL_BANDAR_DAMAI_PERDANA = 621
  KL_BANDAR_MENJALARA = 351
  KL_BANDAR_TASIK_SELATAN = 352
  KL_BANGSAR = 353
  KL_BANGSAR_SOUTH = 354
  KL_BATU = 355
  KL_BRICKFIELDS = 356
  KL_BUKIT_BINTANG = 357
  KL_BUKIT_JALIL = 358
  KL_BUKIT_LEDANG = 359
  KL_BUKIT_PERSEKUTUAN = 624
  KL_BUKIT_TUNKU = 623
  KL_CHERAS = 360
  KL_CITY_CENTRE = 361
  KL_COUNTRY_HEIGHTS = 362
  KL_COUNTRY_HEIGHTS_DAMANSARA = 363
  KL_DAMANSARA = 364
  KL_DAMANSARA_HEIGHTS = 365
  KL_DESA_PANDAN = 366
  KL_DESA_PARKCITY = 367
  KL_DESA_PETALING = 368
  KL_GOMBAK = 369
  KL_JALAN_AMPANG = 639
  KL_JALAN_IPOH = 370
  KL_JALAN_KUCHING = 371
  KL_JALAN_SULTAN_ISMAIL = 372
  KL_JINJANG = 373
  KL_KENNY_HILLS = 374
  KL_KEPONG = 375
  KL_KERAMAT = 376
  KL_KL_CITY = 377
  KL_KL_SENTRAL = 378
  KL_KLCC = 379
  KL_KUCHAI_LAMA = 380
  KL_MID_VALLEY_CITY = 381
  KL_MONT_KIARA = 382
  KL_OLD_KLANG_ROAD = 383
  KL_OUG = 384
  KL_PANDAN_INDAH = 385
  KL_PANDAN_JAYA = 386
  KL_PANDAN_PERDANA = 622
  KL_PANTAI = 387
  KL_PEKAN_BATU = 388
  KL_PUCHONG = 389
  KL_SALAK_SELATAN = 390
  KL_SEGAMBUT = 391
  KL_SENTUL = 392
  KL_SEPUTEH = 393
  KL_SERDANG = 394
  KL_SETAPAK = 395
  KL_SETIA_ECO_PARK = 396
  KL_SETIAWANGSA = 626
  KL_SOLARIS_DUTAMAS = 397
  KL_SRI_DAMANSARA = 398
  KL_SRI_HARTAMAS = 399
  KL_SRI_PETALING = 400
  KL_SUNGAI_BESI = 401
  KL_SUNGAI_PENCHALA = 402
  KL_TAMAN_DESA = 403
  KL_TAMAN_DUTA = 404
  KL_TAMAN_MELAWATI = 405
  KL_TAMAN_TUN_DR_ISMAIL = 406
  KL_TAMAN_PERMATA = 645
  KL_TITIWANGSA = 627
  KL_TPM = 407
  KL_WANGSA_MAJU = 408
  KL_OTHERS = 409