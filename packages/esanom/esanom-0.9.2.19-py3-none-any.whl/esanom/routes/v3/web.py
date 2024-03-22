
#################################################################################
#
# {___     {__          {__       {__
# {_ {__   {__          {_ {__   {___
# {__ {__  {__   {__    {__ {__ { {__
# {__  {__ {__ {__  {__ {__  {__  {__
# {__   {_ {__{__    {__{__   {_  {__
# {__    {_ __ {__  {__ {__       {__
# {__      {__   {__    {__       {__
#
# (C) Copyright European Space Agency, 2024
# 
# This file is subject to the terms and conditions defined in file 'LICENCE.txt', 
# which is part of this source code package. No part of the package, including 
# this file, may be copied, modified, propagated, or distributed except 
# according to the terms contained in the file ‘LICENCE.txt’.“ 
#
#################################################################################

import time
import json
import random
from importlib.metadata import version
from flask import current_app , Blueprint , Response , render_template
from esanom import database as _database , util as _util , pipeline as _pipeline , config as _config, version as _version
from . import common as _common

#####################################################################

ROUTES = Blueprint( "routes" , __name__ , template_folder = "templates" , static_folder='static' )

#####################################################################

@ROUTES.route( "/" , methods = [ "GET" ] )
def index( ) :
    return( render_template( "index.html" ) )
    
#####################################################################

@ROUTES.route( "/error_404" , methods = [ "GET" ] )
def error_404( ) :
    return( render_template( "error_404.html" ) , 404 )

@ROUTES.route( "/error_500" , methods = [ "GET" ] )
def error_500( ) :
    return( render_template( "error_500.html" ) , 500 )

#####################################################################

@ROUTES.app_context_processor
def app_context_processor( ) :
    data = {
        "server_security_lax" : _config.DATA[ "server_security_lax" ] ,
        "version" : version( "esanom" ) ,
        "time" : time.time()
    }
    return( dict( _tdata = data ) )

@ROUTES.app_template_global( "test" )
def app_template_global_test( n ) :
    return( f"{n}." )

#####################################################################

@ROUTES.route( "/admin/db_rolemodel_rows" , methods = [ "GET" ] )
def admin_db_rolemodel_rows( ) :

    rolemodel_rows = _database.db_query_select_rows( "SELECT id,api_id,name,enable,updateable from rolemodel order by id" )

    print(rolemodel_rows)

    for rolemodel_row in rolemodel_rows :

        rolemodel_api_id = rolemodel_row[ "api_id" ]

        if rolemodel_api_id == None : continue

        api_row = _database.db_query_select_row( "SELECT * from api where id=%s LIMIT 1" , [ rolemodel_api_id ] )
        api_name = api_row[ "name" ]
        if api_name.startswith( "test_" ) : api_name = api_name[ -10: ]

        rolemodel_row[ "[api_name]" ] = api_name
        rolemodel_row[ "[api_enable]" ] = api_row[ "enable" ]

    tdata = {
        "rolemodel_rows" : rolemodel_rows
    }
    print(tdata)

    return( render_template( "db_rolemodel_rows.html" , tdata = tdata ) )

@ROUTES.route( "/admin/db_rolemodel_row" , methods = [ "GET" ] )
def admin_db_rolemodel_row( ) :

    rolemodel_id = _common.request_arg_int( "rolemodel_id" )

    ####

    rolemodel_row = _database.db_query_select_row( "SELECT id,api_id,name,enable,updateable from rolemodel where id=%s" , [ rolemodel_id ] )

    mport_rows = _database.db_query_select_rows( "SELECT id,port_id,direction,enable,cardinal from mport where rolemodel_id=%s order by id" , [ rolemodel_id ] )

    mpins=[]
    for mport_row in mport_rows :
        port_row = _database.db_query_select_row( "SELECT * from port where id=%s LIMIT 1" , [ mport_row["port_id"]] )
        port_name = port_row[ "name" ]
        mport_row["[port_name]"]=port_name

        mpin_rows = _database.db_query_select_rows( "SELECT id,mport_id,unit_id from mpin where mport_id=%s order by id" , [ mport_row["id"] ] )

        for mpin_row in mpin_rows :
            unit_row = _database.db_query_select_row( "SELECT * from unit where id=%s LIMIT 1" , [ mpin_row["unit_id"]] )
            pin_row = _database.db_query_select_row( "SELECT * from pin where id=%s LIMIT 1" , [ unit_row["pin_id"]] )
            port_pin_row = _database.db_query_select_row( "SELECT * from port_pin where port_id=%s and pin_id=%s LIMIT 1" , [port_row["id"], pin_row["id"]] )
            mpin_row["[direction]"]=mport_row["direction"]
            mpin_row["[port_pin_cardinal]"]=port_pin_row["cardinal"]
            mpin_row["[pin_id]"]=pin_row["id"]
            mpin_row["[port_name/pin_name(unit_name)]"]=port_row["name"]+"/"+pin_row["name"]+"("+unit_row["name"]+")"


        mpins.append(mpin_rows)


    tdata = {
        "rolemodel_row" : rolemodel_row ,
        "mport_rows" : mport_rows ,
        "mpins" : mpins
    }

    return( render_template( "db_rolemodel_row.html" ,  tdata = tdata ) )

####

@ROUTES.route( "/admin/db_pipeline_rows" , methods = [ "GET" ] )
def admin_db_pipeline_rows( ) :

    pipeline_rows = _database.db_query_select_rows( "SELECT id,roleuser_id,name,status,done,archived,created_at,updated_at from pipeline order by id DESC" )

    tdata = {
        "pipeline_rows" : pipeline_rows
    }

    return( render_template( "admin_db_pipeline_rows.html" , tdata = tdata ) )

@ROUTES.route( "/admin/db_pipeline_row" , methods = [ "GET" ] )
def admin_db_pipeline_row( ) :
    pipeline_id = _common.request_arg_int( "pipeline_id" )
    pipeline_row = _database.db_query_select_row( "SELECT * from pipeline where id=%s" , [pipeline_id] )

    pipeline_object = _database.pipeline_object(pipeline_row)

    tdata = {
        "pipeline_row" : pipeline_row ,
        "pipeline" : pipeline_object
    }
    pipeline_object.print_debug()
    return( render_template( "admin_db_pipeline_row.html" , tdata = tdata ) )


