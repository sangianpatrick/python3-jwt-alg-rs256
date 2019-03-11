from jwt import JWT, jwk_from_pem, jwk, jwk_from_dict
import time

payload = {
    'iss': 'https://patrick-test.com/',
    'sub': '14qwafzx',
    'iat': int(time.time()),
    'exp': int(time.time()) + 60*60*24*1,
}

def generate_credential(**payload):
  jwt = JWT()
  with open('private.pem', 'rb') as fh:
    private_key = jwk_from_pem(fh.read())
  token = jwt.encode(payload, private_key, 'RS256')
  return token

def verify_token(token):
  jwt = JWT()
  with open('public.pem', 'rb') as fh:
    public_key = jwk_from_pem(fh.read())
  
  payload = jwt.decode(token, public_key)
  return payload
  

# print(generate_credential(**payload))

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiAiaHR0cHM6Ly9wYXRyaWNrLXRlc3QuY29tLyIsICJzdWIiOiAiMTRxd2FmengiLCAiaWF0IjogMTU1MjM0MDk1NCwgImV4cCI6IDE1NTI0MjczNTR9.fHsvsWp4-5NHzVHqu4klAlbJu-U_FnvyphlPfnXrb3xQdSIN-BmRfYkGvmOmWt_6tED6ZkGuRz4B-5Ot5fvdjV_n2HMpZrZagaHwVbMzlBmZuTIu0eEpMIDdLadgfFVacatT0uKCPlvdLrbvOzZs6-HhM131Xn4_sh3ul-o5-cBIpvMnRBkJd2DlvZ8p9vwEa46bv2vmdR8yokGKWQTPz3LaO7rK1pMfJnePC-gYp0C6AuBH2iiqiW-ZNog02QMJVJzxagsJ13YqKTbiNnvNO_JI8yXxWzfNgKZYOUw-0pPmIMBYYLqw7trKtJy7D7H4XrG68rIZa2w50SLmcJeCR13WF5iRuA-g22F5P6tnjZPCBeXI4Dx9rUyfTSV5zFIo18C-WciSF3f8DYDiwqe6ibIFLfQxH55914c-q5Cvu-yZM9KBSkqOPHC4xh8I9e276b5Y0E56r9oQNM3nYs3ibiciOGUzdOb3YC1or32cDAOKxUJHEzuIAwQpa7eZ072gh6nJTZrWIdc-vusBm1AhvXbiDw4DfWIZbMAGHpLlP2POi_TUMD3_VA6UjuA777QnPvw7pdaflq4TmE7_bY6nycgQ5xS70MDR1MS3Ol-fwijVEJU0ppQvdtxuh3TM9zYj-NARNJ6OWqlUtJmo7PXp9jWuhK5dNDdtD-YjH_UaNIg'

print(verify_token(token))