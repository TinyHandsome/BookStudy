import 'api.dart';
import '../data/gozero_code-api.dart';

/// gozero_code-api

/// --/from/:name--
///
/// request: Request
/// response: Response
Future gozeroCode(
	String name,
	
    {Function(Response)? ok,
    Function(String)? fail,
    Function? eventually}) async {
  await apiGet("/from/${name}",
  	 ok: (data) {
    if (ok != null) ok(Response.fromJson(data));
  }, fail: fail, eventually: eventually);
}

/// --/user--
///
/// request: 
/// response: Response
Future user(
	
	
    {Function(Response)? ok,
    Function(String)? fail,
    Function? eventually}) async {
  await apiGet("/user",
  	 ok: (data) {
    if (ok != null) ok(Response.fromJson(data));
  }, fail: fail, eventually: eventually);
}

