nameyear
========

Simple python dictionary derived from United States Social Security Admnistration - Popular Baby Names: http://www.ssa.gov/oact/babynames/limits.html. I fully recognize there is no right answer as to which gender a name is (or even what "gender" means), but this can still be useful for stats purposes.

    import nameyear
    myname = u'Philip'
    mygender = u'M'
    print nameyear.nameyear[myname.upper()][mygender.upper()]

