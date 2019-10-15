"""
Souffle - A Datalog Compiler
Copyright (c) 2017, The Souffle Developers. All rights reserved
Licensed under the Universal Permissive License v 1.0 as shown at:
- https://opensource.org/licenses/UPL
- <souffle root>/licenses/SOUFFLE-UPL.txt
"""

import SwigInterface
p = SwigInterface.newInstance('movies')
p.loadAll('.')
p.run()
p.printAll('.')
p.thisown=1
del p