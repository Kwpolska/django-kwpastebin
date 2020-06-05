# Generated by Django 3.0.7 on 2020-06-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwpastebin', '0007_auto_20200229_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='language',
            field=models.CharField(choices=[('abap', 'ABAP'), ('abnf', 'ABNF'), ('as', 'ActionScript'), ('as3', 'ActionScript 3'), ('ada', 'Ada'), ('adl', 'ADL'), ('agda', 'Agda'), ('aheui', 'Aheui'), ('alloy', 'Alloy'), ('at', 'AmbientTalk'), ('ampl', 'Ampl'), ('ng2', 'Angular2'), ('antlr', 'ANTLR'), ('antlr-as', 'ANTLR With ActionScript Target'), ('antlr-csharp', 'ANTLR With C# Target'), ('antlr-cpp', 'ANTLR With CPP Target'), ('antlr-java', 'ANTLR With Java Target'), ('antlr-objc', 'ANTLR With ObjectiveC Target'), ('antlr-perl', 'ANTLR With Perl Target'), ('antlr-python', 'ANTLR With Python Target'), ('antlr-ruby', 'ANTLR With Ruby Target'), ('apacheconf', 'ApacheConf'), ('apl', 'APL'), ('applescript', 'AppleScript'), ('arduino', 'Arduino'), ('aspectj', 'AspectJ'), ('aspx-cs', 'aspx-cs'), ('aspx-vb', 'aspx-vb'), ('asy', 'Asymptote'), ('augeas', 'Augeas'), ('ahk', 'autohotkey'), ('autoit', 'AutoIt'), ('awk', 'Awk'), ('basemake', 'Base Makefile'), ('bash', 'Bash'), ('console', 'Bash Session'), ('bat', 'Batchfile'), ('bbcbasic', 'BBC Basic'), ('bbcode', 'BBCode'), ('bc', 'BC'), ('befunge', 'Befunge'), ('bib', 'BibTeX'), ('blitzbasic', 'BlitzBasic'), ('blitzmax', 'BlitzMax'), ('bnf', 'BNF'), ('boa', 'Boa'), ('boo', 'Boo'), ('boogie', 'Boogie'), ('brainfuck', 'Brainfuck'), ('bst', 'BST'), ('bugs', 'BUGS'), ('c', 'C'), ('csharp', 'C#'), ('cpp', 'C++'), ('c-objdump', 'c-objdump'), ('ca65', 'ca65 assembler'), ('cadl', 'cADL'), ('camkes', 'CAmkES'), ('capnp', "Cap'n Proto"), ('capdl', 'CapDL'), ('cbmbas', 'CBM BASIC V2'), ('ceylon', 'Ceylon'), ('cfengine3', 'CFEngine3'), ('cfs', 'cfstatement'), ('chai', 'ChaiScript'), ('chapel', 'Chapel'), ('charmci', 'Charmci'), ('cheetah', 'Cheetah'), ('cirru', 'Cirru'), ('clay', 'Clay'), ('clean', 'Clean'), ('clojure', 'Clojure'), ('clojurescript', 'ClojureScript'), ('cmake', 'CMake'), ('cobol', 'COBOL'), ('cobolfree', 'COBOLFree'), ('coffee-script', 'CoffeeScript'), ('cfc', 'Coldfusion CFC'), ('cfm', 'Coldfusion HTML'), ('common-lisp', 'Common Lisp'), ('componentpascal', 'Component Pascal'), ('coq', 'Coq'), ('cpp-objdump', 'cpp-objdump'), ('cpsa', 'CPSA'), ('crmsh', 'Crmsh'), ('croc', 'Croc'), ('cryptol', 'Cryptol'), ('cr', 'Crystal'), ('csound-document', 'Csound Document'), ('csound', 'Csound Orchestra'), ('csound-score', 'Csound Score'), ('css', 'CSS'), ('css+django', 'CSS+Django/Jinja'), ('css+genshitext', 'CSS+Genshi Text'), ('css+lasso', 'CSS+Lasso'), ('css+mako', 'CSS+Mako'), ('css+mozpreproc', 'CSS+mozpreproc'), ('css+myghty', 'CSS+Myghty'), ('css+php', 'CSS+PHP'), ('css+erb', 'CSS+Ruby'), ('css+smarty', 'CSS+Smarty'), ('cuda', 'CUDA'), ('cypher', 'Cypher'), ('cython', 'Cython'), ('d', 'D'), ('d-objdump', 'd-objdump'), ('dpatch', 'Darcs Patch'), ('dart', 'Dart'), ('dasm16', 'DASM16'), ('control', 'Debian Control file'), ('sourceslist', 'Debian Sourcelist'), ('delphi', 'Delphi'), ('dg', 'dg'), ('diff', 'Diff'), ('django', 'Django/Jinja'), ('docker', 'Docker'), ('dtd', 'DTD'), ('duel', 'Duel'), ('dylan', 'Dylan'), ('dylan-console', 'Dylan session'), ('dylan-lid', 'DylanLID'), ('email', 'E-mail'), ('earl-grey', 'Earl Grey'), ('easytrieve', 'Easytrieve'), ('ebnf', 'EBNF'), ('ec', 'eC'), ('ecl', 'ECL'), ('eiffel', 'Eiffel'), ('elixir', 'Elixir'), ('iex', 'Elixir iex session'), ('elm', 'Elm'), ('emacs', 'EmacsLisp'), ('ragel-em', 'Embedded Ragel'), ('erb', 'ERB'), ('erlang', 'Erlang'), ('erl', 'Erlang erl session'), ('evoque', 'Evoque'), ('ezhil', 'Ezhil'), ('fsharp', 'F#'), ('factor', 'Factor'), ('fancy', 'Fancy'), ('fan', 'Fantom'), ('felix', 'Felix'), ('fennel', 'Fennel'), ('fish', 'Fish'), ('flatline', 'Flatline'), ('floscript', 'FloScript'), ('forth', 'Forth'), ('fortran', 'Fortran'), ('fortranfixed', 'FortranFixed'), ('foxpro', 'FoxPro'), ('freefem', 'Freefem'), ('gap', 'GAP'), ('gas', 'GAS'), ('genshi', 'Genshi'), ('genshitext', 'Genshi Text'), ('pot', 'Gettext Catalog'), ('cucumber', 'Gherkin'), ('glsl', 'GLSL'), ('gnuplot', 'Gnuplot'), ('go', 'Go'), ('golo', 'Golo'), ('gooddata-cl', 'GoodData-CL'), ('gosu', 'Gosu'), ('gst', 'Gosu Template'), ('groff', 'Groff'), ('groovy', 'Groovy'), ('haml', 'Haml'), ('handlebars', 'Handlebars'), ('haskell', 'Haskell'), ('hx', 'Haxe'), ('hexdump', 'Hexdump'), ('hlsl', 'HLSL'), ('hsail', 'HSAIL'), ('hspec', 'Hspec'), ('html', 'HTML'), ('html+ng2', 'HTML + Angular2'), ('html+cheetah', 'HTML+Cheetah'), ('html+django', 'HTML+Django/Jinja'), ('html+evoque', 'HTML+Evoque'), ('html+genshi', 'HTML+Genshi'), ('html+handlebars', 'HTML+Handlebars'), ('html+lasso', 'HTML+Lasso'), ('html+mako', 'HTML+Mako'), ('html+myghty', 'HTML+Myghty'), ('html+php', 'HTML+PHP'), ('html+smarty', 'HTML+Smarty'), ('html+twig', 'HTML+Twig'), ('html+velocity', 'HTML+Velocity'), ('http', 'HTTP'), ('haxeml', 'Hxml'), ('hylang', 'Hy'), ('hybris', 'Hybris'), ('icon', 'Icon'), ('idl', 'IDL'), ('idris', 'Idris'), ('igor', 'Igor'), ('inform6', 'Inform 6'), ('i6t', 'Inform 6 template'), ('inform7', 'Inform 7'), ('ini', 'INI'), ('io', 'Io'), ('ioke', 'Ioke'), ('irc', 'IRC logs'), ('isabelle', 'Isabelle'), ('j', 'J'), ('jags', 'JAGS'), ('jasmin', 'Jasmin'), ('java', 'Java'), ('jsp', 'Java Server Page'), ('js', 'JavaScript'), ('js+cheetah', 'JavaScript+Cheetah'), ('js+django', 'JavaScript+Django/Jinja'), ('js+genshitext', 'JavaScript+Genshi Text'), ('js+lasso', 'JavaScript+Lasso'), ('js+mako', 'JavaScript+Mako'), ('javascript+mozpreproc', 'Javascript+mozpreproc'), ('js+myghty', 'JavaScript+Myghty'), ('js+php', 'JavaScript+PHP'), ('js+erb', 'JavaScript+Ruby'), ('js+smarty', 'JavaScript+Smarty'), ('jcl', 'JCL'), ('jsgf', 'JSGF'), ('json', 'JSON'), ('jsonld', 'JSON-LD'), ('json-object', 'JSONBareObject'), ('julia', 'Julia'), ('jlcon', 'Julia console'), ('juttle', 'Juttle'), ('kal', 'Kal'), ('kconfig', 'Kconfig'), ('kmsg', 'Kernel log'), ('koka', 'Koka'), ('kotlin', 'Kotlin'), ('lasso', 'Lasso'), ('lean', 'Lean'), ('less', 'LessCss'), ('lighty', 'Lighttpd configuration file'), ('limbo', 'Limbo'), ('liquid', 'liquid'), ('lagda', 'Literate Agda'), ('lcry', 'Literate Cryptol'), ('lhs', 'Literate Haskell'), ('lidr', 'Literate Idris'), ('live-script', 'LiveScript'), ('llvm', 'LLVM'), ('llvm-mir', 'LLVM-MIR'), ('llvm-mir-body', 'LLVM-MIR Body'), ('logos', 'Logos'), ('logtalk', 'Logtalk'), ('lsl', 'LSL'), ('lua', 'Lua'), ('make', 'Makefile'), ('mako', 'Mako'), ('maql', 'MAQL'), ('md', 'markdown'), ('markdown_kwpastebin', 'markdown (render)'), ('mask', 'Mask'), ('mason', 'Mason'), ('mathematica', 'Mathematica'), ('matlab', 'Matlab'), ('matlabsession', 'Matlab session'), ('mime', 'MIME'), ('minid', 'MiniD'), ('ms', 'MiniScript'), ('modelica', 'Modelica'), ('modula2', 'Modula-2'), ('trac-wiki', 'MoinMoin/Trac Wiki markup'), ('monkey', 'Monkey'), ('monte', 'Monte'), ('moocode', 'MOOCode'), ('moon', 'MoonScript'), ('mosel', 'Mosel'), ('mozhashpreproc', 'mozhashpreproc'), ('mozpercentpreproc', 'mozpercentpreproc'), ('mql', 'MQL'), ('mscgen', 'Mscgen'), ('doscon', 'MSDOS Session'), ('mupad', 'MuPAD'), ('mxml', 'MXML'), ('myghty', 'Myghty'), ('mysql', 'MySQL'), ('nasm', 'NASM'), ('ncl', 'NCL'), ('nemerle', 'Nemerle'), ('nesc', 'nesC'), ('newlisp', 'NewLisp'), ('newspeak', 'Newspeak'), ('nginx', 'Nginx configuration file'), ('nim', 'Nimrod'), ('nit', 'Nit'), ('nixos', 'Nix'), ('notmuch', 'Notmuch'), ('nsis', 'NSIS'), ('numpy', 'NumPy'), ('nusmv', 'NuSMV'), ('objdump', 'objdump'), ('objdump-nasm', 'objdump-nasm'), ('objective-c', 'Objective-C'), ('objective-c++', 'Objective-C++'), ('objective-j', 'Objective-J'), ('ocaml', 'OCaml'), ('octave', 'Octave'), ('odin', 'ODIN'), ('ooc', 'Ooc'), ('opa', 'Opa'), ('openedge', 'OpenEdge ABL'), ('pacmanconf', 'PacmanConf'), ('pan', 'Pan'), ('parasail', 'ParaSail'), ('pawn', 'Pawn'), ('peg', 'PEG'), ('perl', 'Perl'), ('perl6', 'Perl6'), ('php', 'PHP'), ('pig', 'Pig'), ('pike', 'Pike'), ('pkgconfig', 'PkgConfig'), ('plpgsql', 'PL/pgSQL'), ('pony', 'Pony'), ('psql', 'PostgreSQL console (psql)'), ('postgresql', 'PostgreSQL SQL dialect'), ('postscript', 'PostScript'), ('pov', 'POVRay'), ('powershell', 'PowerShell'), ('ps1con', 'PowerShell Session'), ('praat', 'Praat'), ('prolog', 'Prolog'), ('properties', 'Properties'), ('protobuf', 'Protocol Buffer'), ('pug', 'Pug'), ('puppet', 'Puppet'), ('pypylog', 'PyPy Log'), ('python', 'Python'), ('python2', 'Python 2.x'), ('py2tb', 'Python 2.x Traceback'), ('pycon', 'Python console session'), ('pytb', 'Python Traceback'), ('qbasic', 'QBasic'), ('qml', 'QML'), ('qvto', 'QVTO'), ('racket', 'Racket'), ('ragel', 'Ragel'), ('ragel-c', 'Ragel in C Host'), ('ragel-cpp', 'Ragel in CPP Host'), ('ragel-d', 'Ragel in D Host'), ('ragel-java', 'Ragel in Java Host'), ('ragel-objc', 'Ragel in Objective C Host'), ('ragel-ruby', 'Ragel in Ruby Host'), ('raw', 'Raw token data'), ('rconsole', 'RConsole'), ('rd', 'Rd'), ('reason', 'ReasonML'), ('rebol', 'REBOL'), ('red', 'Red'), ('redcode', 'Redcode'), ('registry', 'reg'), ('rnc', 'Relax-NG Compact'), ('resource', 'ResourceBundle'), ('rst', 'reStructuredText'), ('rexx', 'Rexx'), ('rhtml', 'RHTML'), ('ride', 'Ride'), ('roboconf-graph', 'Roboconf Graph'), ('roboconf-instances', 'Roboconf Instances'), ('robotframework', 'RobotFramework'), ('spec', 'RPMSpec'), ('rql', 'RQL'), ('rsl', 'RSL'), ('rb', 'Ruby'), ('rbcon', 'Ruby irb session'), ('rust', 'Rust'), ('splus', 'S'), ('sarl', 'SARL'), ('sas', 'SAS'), ('sass', 'Sass'), ('scala', 'Scala'), ('ssp', 'Scalate Server Page'), ('scaml', 'Scaml'), ('scdoc', 'scdoc'), ('scheme', 'Scheme'), ('scilab', 'Scilab'), ('scss', 'SCSS'), ('shen', 'Shen'), ('shexc', 'ShExC'), ('sieve', 'Sieve'), ('silver', 'Silver'), ('slash', 'Slash'), ('slim', 'Slim'), ('slurm', 'Slurm'), ('smali', 'Smali'), ('smalltalk', 'Smalltalk'), ('sgf', 'SmartGameFormat'), ('smarty', 'Smarty'), ('snobol', 'Snobol'), ('snowball', 'Snowball'), ('solidity', 'Solidity'), ('sp', 'SourcePawn'), ('sparql', 'SPARQL'), ('sql', 'SQL'), ('sqlite3', 'sqlite3con'), ('squidconf', 'SquidConf'), ('stan', 'Stan'), ('sml', 'Standard ML'), ('stata', 'Stata'), ('sc', 'SuperCollider'), ('swift', 'Swift'), ('swig', 'SWIG'), ('systemverilog', 'systemverilog'), ('tads3', 'TADS 3'), ('tap', 'TAP'), ('tasm', 'TASM'), ('tcl', 'Tcl'), ('tcsh', 'Tcsh'), ('tcshcon', 'Tcsh Session'), ('tea', 'Tea'), ('ttl', 'Tera Term macro'), ('termcap', 'Termcap'), ('terminfo', 'Terminfo'), ('terraform', 'Terraform'), ('tex', 'TeX'), ('text', 'Text only'), ('thrift', 'Thrift'), ('todotxt', 'Todotxt'), ('toml', 'TOML'), ('rts', 'TrafficScript'), ('tsql', 'Transact-SQL'), ('treetop', 'Treetop'), ('turtle', 'Turtle'), ('twig', 'Twig'), ('ts', 'TypeScript'), ('typoscript', 'TypoScript'), ('typoscriptcssdata', 'TypoScriptCssData'), ('typoscripthtmldata', 'TypoScriptHtmlData'), ('ucode', 'ucode'), ('unicon', 'Unicon'), ('urbiscript', 'UrbiScript'), ('usd', 'USD'), ('vala', 'Vala'), ('vb.net', 'VB.net'), ('vbscript', 'VBScript'), ('vcl', 'VCL'), ('vclsnippets', 'VCLSnippets'), ('vctreestatus', 'VCTreeStatus'), ('velocity', 'Velocity'), ('verilog', 'verilog'), ('vgl', 'VGL'), ('vhdl', 'vhdl'), ('vim', 'VimL'), ('wdiff', 'WDiff'), ('webidl', 'Web IDL'), ('whiley', 'Whiley'), ('x10', 'X10'), ('xml', 'XML'), ('xml+cheetah', 'XML+Cheetah'), ('xml+django', 'XML+Django/Jinja'), ('xml+evoque', 'XML+Evoque'), ('xml+lasso', 'XML+Lasso'), ('xml+mako', 'XML+Mako'), ('xml+myghty', 'XML+Myghty'), ('xml+php', 'XML+PHP'), ('xml+erb', 'XML+Ruby'), ('xml+smarty', 'XML+Smarty'), ('xml+velocity', 'XML+Velocity'), ('xorg.conf', 'Xorg'), ('xquery', 'XQuery'), ('xslt', 'XSLT'), ('xtend', 'Xtend'), ('extempore', 'xtlang'), ('xul+mozpreproc', 'XUL+mozpreproc'), ('yaml', 'YAML'), ('yaml+jinja', 'YAML+Jinja'), ('zeek', 'Zeek'), ('zephir', 'Zephir'), ('zig', 'Zig')], default='text', max_length=100),
        ),
    ]
