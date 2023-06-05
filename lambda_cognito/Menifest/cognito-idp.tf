resource "aws_cognito_user_pool" "pool"{
    alias_attributes = [ "email" ]
    auto_verified_attributes = [ "email" ]
    mfa_configuration = "OFF"
    name = "test"
    password_policy {
      minimum_length = 8
      require_lowercase = true
      require_uppercase = true
      require_symbols = true
      require_numbers = true
    }
}