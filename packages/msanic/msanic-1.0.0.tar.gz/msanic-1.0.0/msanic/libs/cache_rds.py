from abc import abstractmethod

from msanic.libs.base_conf import BaseConf
from msanic.libs.base_model import DbModel
from msanic.tool import json_parse


class JsonRC:

    db_model: DbModel = None
    rds: BaseConf = None

    @classmethod
    @abstractmethod
    async def fun_set_cache(cls, info: dict) -> dict:
        pass

    @classmethod
    async def get_cache_by_pk(cls, pk_val: (int, str)):
        async def from_db():
            db_info = await cls.db_model.get_by_pk(pk_val)
            if db_info:
                pinfo = await cls.fun_set_cache(db_info)
                return pinfo
            return
        if not cls.db_model:
            return
        info = await cls.rds.get_hash(cls.db_model.sheet_name(), pk_val)
        if info:
            return json_parse(info)
        p_info = await cls.rds.locked(cls.db_model.sheet_name(), from_db)
        return p_info

    @classmethod
    async def get_cache_by_unique(cls, unique_val, unique_field: str, key_name: str):
        async def from_db():
            info = await cls.db_model.get_from_dict({unique_field: unique_val})
            if info:
                return await cls.fun_set_cache(info)
            return

        if not cls.db_model:
            return
        item_id = await cls.rds.get_hash(key_name, unique_val)
        if item_id:
            return await cls.get_cache_by_pk(item_id)
        return await cls.rds.locked(cls.db_model.sheet_name(), fun=from_db)

    @classmethod
    async def query_map(cls, is_super=False, field_name='name', groups: (list, tuple) = None, group_key='gid'):
        async def from_db():
            data_list = await cls.db_model.get_from_dict({})
            return [await cls.fun_set_cache(info) for n in data_list]

        if not groups:
            groups = []
        if not cls.db_model:
            return []
        pk_name = cls.db_model.pk_name()
        all_items = await cls.rds.get_hash_vals(cls.db_model.sheet_name())
        if not all_items:
            all_items = await cls.rds.locked(cls.db_model.sheet_name(), fun=from_db, time_out=5)
        if (not is_super) and cls.db_model.check_field(group_key):
            new_list = []
            for item in all_items:
                info = json_parse(item)
                g_id = info.get(group_key)
                (g_id in groups) and new_list.append({
                    'label': info.get(field_name), 'value': info.get(pk_name), group_key: g_id})
            return new_list
        return [{'label': info.get(field_name), 'value': info.get(pk_name), group_key: info.get(group_key)}
                for item in all_items if (info := json_parse(item))]

    @classmethod
    async def get_name(cls, pk_id: int or str, name_field='name'):
        if not pk_id:
            return '-'
        info = await cls.get_cache_by_pk(pk_id)
        return info.get(name_field) if info else '-'

    @classmethod
    async def get_map(cls, pk_id: int or str, name_list: list or tuple = None):
        if not pk_id:
            return {}
        info = await cls.get_cache_by_pk(pk_id)
        return {name: info.get(name) for name in name_list} if info else {}
