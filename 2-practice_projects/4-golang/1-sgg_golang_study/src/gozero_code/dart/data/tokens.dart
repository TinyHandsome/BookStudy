class Tokens {
  /// the token used to access, it must be carried in the header of each request
  final String accessToken;
  final int accessExpire;

  /// the token used to refresh
  final String refreshToken;
  final int refreshExpire;
  final int refreshAfter;
  Tokens({
		required this.accessToken,
		required this.accessExpire,
		required this.refreshToken,
		required this.refreshExpire,
		required this.refreshAfter
	});
  factory Tokens.fromJson(Map<String, dynamic> m) {
    return Tokens(
        accessToken: m['access_token'],
        accessExpire: m['access_expire'],
        refreshToken: m['refresh_token'],
        refreshExpire: m['refresh_expire'],
        refreshAfter: m['refresh_after']);
  }
  Map<String, dynamic> toJson() {
    return {
      'access_token': accessToken,
      'access_expire': accessExpire,
      'refresh_token': refreshToken,
      'refresh_expire': refreshExpire,
      'refresh_after': refreshAfter,
    };
  }
}
