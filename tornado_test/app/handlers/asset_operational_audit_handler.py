#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : asset_operational_audit_handler.py
# @Author: Fred Yangxiaofei
# @Date  : 2019/9/11
# @Role  : 资产操作记录


from models.server import model_to_dict, AssetOperationalAudit
from websdk.db_context import DBContext
from sqlalchemy import or_

with DBContext('r') as session:
    log_info = session.query(AssetOperationalAudit).filter(
        AssetOperationalAudit.ctime > start_time_tuple,
        AssetOperationalAudit.ctime < end_time_tuple).order_by(
        -AssetOperationalAudit.ctime).offset(limit_start).limit(int(limit))
    session.query(Server).filter(or_(Server.hostname.like('%{}%'.format(key)),

                                     Server.state.like('%{}%'.format(key)))).order_by(Server.id)


with DBContext('w', None, True) as session:
    new_server = Server(hostname=hostname, ip=ip, public_ip=public_ip, port=int(port), idc=idc,
                        admin_user=admin_user, region=region, state=state, detail=detail)
    session.add(new_server)

    all_tags = session.query(Tag.id).filter(Tag.tag_name.in_(tag_list)).order_by(Tag.id).all()
    # print('all_tags', all_tags)
    if all_tags:
        for tag_id in all_tags:
            session.add(ServerTag(server_id=new_server.id, tag_id=tag_id[0]))
with DBContext('w', None, True) as session:
    exist_hostname = session.query(Server.hostname).filter(Server.id == server_id).first()
    if exist_hostname[0] != hostname:
        return self.write(dict(code=-2, msg='主机名不能修改'))

    session.query(ServerTag).filter(ServerTag.server_id == server_id).delete(synchronize_session=False)
    all_tags = session.query(Tag.id).filter(Tag.tag_name.in_(tag_list)).order_by(Tag.id).all()
    if all_tags:
        for tag_id in all_tags:
            session.add(ServerTag(server_id=server_id, tag_id=tag_id[0]))

    session.query(Server).filter(Server.id == server_id).update({Server.hostname: hostname, Server.ip: ip,
                                                                 Server.port: int(port),
                                                                 Server.public_ip: public_ip,
                                                                 Server.idc: idc,
                                                                 Server.admin_user: admin_user,
                                                                 Server.region: region, Server.detail: detail
                                                                 })  # Server.state: 'new'
