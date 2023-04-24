# pyHolon

A framework for Notification Oriented Paradigm (NOP[[1]](#1)) implemented in
TypeScript.

In the Notification Oriented Paradigm (NOP), there are the "factual and causal
smart-entities named as Fact Base Elements (FBEs) and Rules that are related to
another collaborative notifier smart-entities. Each FBE is related to Attributes
and Methods, whereas each Rule to Premises-Conditions and Actions-Instigations.
All these entities collaboratively carry out the inference process using
Notifications, providing solutions to deficiencies of current paradigms"
[[1]](#1).

The NOP, in addition to avoiding temporal and structural code redundancies
through notifications, has a defined inference model. This framework promotes
flexibility of this inference model. This flexibility is provided by a
standardized structure for notifying processing, named Notifying Holon.

## Contents

- [Sample application](#sample-application)
- [Possibilities with notifying holons](#possibilities-with-notifying-holons)
  - [Chain operations](#chain-operations)
  - [Custom inequality operator](#custom-inequality-operator)
  - [Search the history graph](#search-the-history-graph)
- [Instructions to run this project](#instructions-to-run-this-project)
- [References](#references)
- [About](#about)

## Sample application

The example below describes a notifying holons that performs a sum.

```python
from pyholon.core import NotifyinfHolon
```

The `receive` method also has an optional second parameter named `modes`. If
`modes=["RENOTIFICATION"]`, the notification will force an exit notification
even if there is no change in holon state. If `modes=["WEAK"]`, in which the
notification updates the input memory of subsequent holons but does not trigger
activations. If `modes=["STRONG"]` an activation will be forced and `f` will be
reevaluated. It is possible to combine notification modes.

## Possibilities with notifying holons

### Chain operations

It is possible to add the output of one holon as input to another. In the
example below, the output of the holon sum of the example was added as input to
a holon that checks if this sum is greater than 5.

```python
from pyholon.core import NotifyinfHolon
```

### Custom inequality operator

It is possible to create a custom inequality operator to avoid excessively
unnecessary triggering of notifications. In the example below, it is considered
that the modulus of the difference of two values ​​must be greater than 1.

```python
from pyholon.core import NotifyinfHolon
```

### Search the history graph

Saving notifications in a history graph:

```python
from pyholon.core import NotifyinfHolon
from pyholon.storage import InMemoryGraph
```

This graph can be used by the algorithms contained in the "algorithms" module of
the library.

## Instructions to run this project

This repository is encapsulated in a published python package. The library is
separated into 3 modules. The "core" module, the "storage" module and the
"algorithms" module. To use it, just import.

## References

<a id="1">[1]</a> J. M. Simão, C. A. Tacla, P. C. Stadzisz and R. F.
Banaszewski, "Notification Oriented Paradigm (NOP) and Imperative Paradigm: A
Comparative Study," Journal of Software Engineering and Applications, Vol. 5 No.
6, 2012, pp. 402-416. doi: https://www.doi.org/10.4236/jsea.2012.56047

## About

Author: Henrique Emanoel Viana, a Brazilian computer scientist, enthusiast of
web technologies, cel: +55 (41) 99999-4664. URL:
https://sites.google.com/view/henriqueviana

Improvements and suggestions are welcome!
