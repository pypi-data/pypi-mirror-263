from typing import Literal
from vinyl.lib.set_methods import base_join_type as base_join_type
from vinyl.lib.table import VinylTable as VinylTable

def join(left: VinylTable, right: VinylTable, *, auto: bool = True, auto_allow_cross_join: bool = False, on: base_join_type | list[base_join_type] = [], how: Literal['inner', 'left', 'outer', 'right', 'semi', 'anti', 'any_inner', 'any_left', 'left_semi'] = 'inner', lname: str = '', rname: str = '{name}_right') -> VinylTable: ...
def union(first: VinylTable, *rest: VinylTable, distinct: bool = False) -> VinylTable:
    """
    Compute the set union of multiple table expressions.

    Unlike the SQL UNION operator, this function allows for the union of tables with different schemas. If a column is present in one table but not in another, the column will be added to the other table with NULL values.

    If `distinct` is True, the result will contain only distinct rows. If `distinct` is False, the result will contain all rows from all tables, including duplicates.
    """
def difference(first: VinylTable, *rest: VinylTable, distinct: bool = False) -> VinylTable:
    """
    Compute the set difference of multiple table expressions.

    Unlike the SQL EXCEPT operator, this function allows for the difference of tables with different schemas. If a column is present in one table but not in another, the column will be added to the other table with NULL values.

    If `distinct` is True, the result will contain only distinct rows. If `distinct` is False, the result will contain all rows from the first table, including duplicates.
    """
def intersect(first: VinylTable, *rest: VinylTable, distinct: bool = True) -> VinylTable:
    """
    Compute the set intersection of multiple table expressions.

    Unlike the SQL INTERSECT operator, this function allows for the intersection of tables with different schemas. If a column is present in one table but not in another, the column will be added to the other table with NULL values.

    If `distinct` is True, the result will contain only distinct rows. If `distinct` is False, the result will contain all rows that are present in all tables, including duplicates.
    """
