from vastdb import *


class Context:
	tx: int
	_rpc: RPC

	def bucket(name: str) -> Bucket

class Bucket:
	ctx: Context
	name: str

	def schema(name: str) -> Schema

class Schema:
	ctx: Context
	path: str

	def schema(name: str) -> Schema
	def table(name: str) -> Table

class Table:
	ctx: Context
	path: str

	def import_files(...)
	def import_partitioned_files(...)
	def select(...) -> ???


class RPC:
	"""
	INTERNAL STUFF: actually uses requests to send/receive stuff
	Cannot do pagination
	"""

	### We can just copy-paste stuff from api.py

	def single_shot_query_data()
	def single_shot_list_columns()

@contextmanager
def context(access, secret, endpoint):
	rpc = RPC(access, secret, endpoint) # Low-level commands => the user should not use it
	tx = rpc.begin_transaction()
	try:
		yield Context(rpc, tx)
	finally:
		rpc.close_transaction(tx)


with context(access, secret, endpoint) as ctx:  # open/closes tx
	# tx keep-alive?
	b = ctx.bucket("buck") # may raise NotFoundError if bucket is missing

	ctx._rpc.strange_thing???

	b.create_schema("s1")
	b.create_schema("s1/s2")
	b.create_schema("s1/s2/s3")

	iterable_of_schema_objects = b.schemas() # BFS or only top-level?

	s = b.schema("s1/s2/s3") # may raise NotFoundError if schema is missing
	s = b.schema("s1").schema("s2/s3") # may raise NotFoundError if schema is missing
	s = b / "s1" / "s2" / "s3" # may raise NotFoundError if schema is missing

	assert s.schemas() == []

	iterable_of_tables_objects = s.tables()
	t = s.table("t") # /bucket/s1/s2/s3/t under tx

	s.rename()
	s.drop()
	...


	# may take a while - finishes when all files are done
	# if all OK, return None
	# in case of error raise ImportFilesError(failed_files_list=[(path, code, reason)])
	t.import_files(["/buck1/file1", ... "/buck3/file3"])
	t.import_partitioned_files({"/buck1/file1": pa.RecordBatch, ... "/buck3/file3": pa.RecordBatch})

	arrow_schema = t.columns()
	iterable_of_record_batches = t.select(
		column_names: List[str], 
		predicate: ibis.BooleanColumn???,
		limit: int = None,
		config: QueryConfig = None
	)


	t.drop()
	t.rename()
	t.add_column()
	t.drop_column()
	...


class QueryConfig:
	num_of_subsplits: int = 2
	num_of_splits: int = 16?
	# how to load balance between VIPs?
	# we need a new RPC to get the "data_enpoints" VIPs from VAST and then we can round-robin between them?
	# => @alon
	##### list_of_data_endpoints: List[str] = None
	limit_per_sub_split: int = 128k
