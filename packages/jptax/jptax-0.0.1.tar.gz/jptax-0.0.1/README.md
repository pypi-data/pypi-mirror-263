# jptax

*jptax* は日本国内の給与所得者に掛かる税金を計算します。

---

Install jptax using pip:

```shell
pip install jptax
```

社会保険料を計算する。

```python
>>> from jptax.insurance import Insurance
>>> insurance = Insurance()
>>> deduction = insurance.calculate(
...   510000, # 支給額
...   500000, # 標準報酬月額
...   45, # 年齢
...   False, # 役員である
...   "13", # 事業所所在地の都道府県コード
...   "1", # 事業コード（1: 一般の事業 2: 農林水産・清酒製造の事業 3: 建設の事業）
... )
>>> deduction.health # 健康保険料 合算
49900.0
>>> deduction.health_employee # 健康保険料 従業員負担分
24950
>>> deduction.caregiving # 介護保険料 合算
8000.0
>>> deduction.caregiving_employee # 介護保険料 従業員負担分
4000
>>> deduction.pension # 厚生年金保険料 合算
91500
>>> deduction.pension_employee # 厚生年金保険料 従業員負担分
45750
>>> deduction.employment # 雇用保険料 合算
7905.0
>>> deduction.employment_employee # 雇用保険料 従業員負担分
3060
>>> deduction.kids_support # 子ども・子育て拠出金
1800.0
```

[![PyPI - Version](https://img.shields.io/pypi/v/jptax.svg)](https://pypi.org/project/jptax)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jptax.svg)](https://pypi.org/project/jptax)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install jptax
```

## License

`jptax` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
