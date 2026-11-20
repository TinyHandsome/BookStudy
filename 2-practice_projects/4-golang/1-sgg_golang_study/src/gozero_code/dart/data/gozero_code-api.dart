// --.\gozero_code--

class Request {
	
	
	final String name;
  Request({
	  required this.name,
	});
	factory Request.fromJson(Map<String,dynamic> m) {
		return Request(
			
				name: 
					
						m['name'] ?? ""
					
			,
		);
	}
	Map<String,dynamic> toJson() {
		return { 
			'name': 
				
					name
				
			,
		};
	}

	
}

class Response {
	
	
	final String message;
  Response({
	  required this.message,
	});
	factory Response.fromJson(Map<String,dynamic> m) {
		return Response(
			
				message: 
					
						m['message'] ?? ""
					
			,
		);
	}
	Map<String,dynamic> toJson() {
		return { 
			'message': 
				
					message
				
			,
		};
	}

	
}
