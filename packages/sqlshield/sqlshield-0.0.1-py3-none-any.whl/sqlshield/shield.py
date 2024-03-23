from sqlglot import parse_one, exp
from pprint import pprint

class Session():
    def __init__(self, db, params):
        self.database = db
        self.params = params
    
    def generateNativeSQL(self, aSql):
        # prepare_table_map
        tbl_map = {}
        for tbl in self.database.tables:
            tbl_map[tbl.pub_name] = tbl
        
        print("Input: ", aSql)
        def transformer(node):
            if isinstance(node, exp.Table):
                tbl_name = node.this.this
                mtable = tbl_map[tbl_name]
                msql = mtable.get_alias_sql(self.params)
                return parse_one(msql)
            return node
        tree = parse_one(aSql)
        new_tree = tree.transform(transformer)
        return new_tree.sql()
    