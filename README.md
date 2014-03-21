nameyear
========

Simple python dictionary (nameyear.py) derived from United States Social Security Administration - Popular Baby Names: http://www.ssa.gov/oact/babynames/limits.html. I fully recognize there is no right answer as to which gender a name is (or even what "gender" means), but this can still be useful for stats purposes.

    import nameyear
    myname = u'Philip'
    mygender = u'M'
    print nameyear.nameyear[myname.upper()][mygender.upper()]
    
    
Sample codes:
+ get_yob.py gets count of babies per year, given one name and gender
+ plot_yob.py plots count of babies per year, given one name and gender

![plot_yob.py output](https://raw.githubusercontent.com/philshem/nameyear/master/plot_yob.png)
