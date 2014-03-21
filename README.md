nameyear
========

Simple python dictionary derived from Social Security Admnistration - Popular Baby Names (http://www.ssa.gov/oact/babynames/limits.html). Gender is always assigned 'M' or 'F', whatever that means.

    import nameyear
    myname = u'Philip'
    mygender = u'M'
    print nameyear.nameyear[myname.upper()][mygender.upper()]

