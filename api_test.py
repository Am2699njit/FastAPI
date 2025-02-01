import requests as r

hostname = "127.0.0.1"
port = "12501"
url = f"http://{hostname}:{port}/cart"
headers = {"api-key":"this-is-the-api-key"}
count = 0

# Testcase 1
response = r.get(url, params={"cart-id":1})
if response.status_code == 403 and response.json()["status"] == "failure":
    count += 1
else:
    print("Test case 1 failed")

# Testcase 2
response = r.get(url, headers=headers)
if response.status_code == 400 and response.json()["status"] == "failure":
    count += 1
else:
    print("Test case 2 failed")

# Testcase 3
response = r.get(url, headers=headers, params={"cart-id":12345678})
if response.status_code == 400 and response.json()["status"] == "failure":
    count += 1
else:
    print("Test case 3 failed")

# Testcase 4
bananas = {"item-name":"banana", "quantity": 4, "price": 1.09}
apples = {"item-name":"apples", "quantity": 3, "price": .45}
response1 = r.post(url, headers=headers, json=bananas)
if response1.status_code == 200 and "cart-id" in response1.json() and response1.json()["status"] == "success":
    count += 1
    cart_id = response1.json()["cart-id"]
    response2 = r.get(url, headers=headers, params={"cart-id":cart_id})
    output = response2.json()

    if response2.status_code == 200 and output["status"] == "success" and str(cart_id) in output and bananas in output[str(cart_id)]:
        count += 1
        response3 = r.post(url, headers=headers, json=apples)

        if response3.status_code == 200 and "cart-id" in response3.json() and response3.json()["status"] == "success":
            count += 1
            cart_id_2 = response3.json()["cart-id"]
            response4 = r.get(url, headers=headers, params={"cart-id":cart_id_2})
            output = response4.json()

            if response4.status_code == 200 and output["status"] == "success" and str(cart_id_2) in output and apples in output[str(cart_id_2)] and bananas not in output[str(cart_id_2)]:
                count += 1
                apples["cart-id"] = bananas["cart-id"] = cart_id
                r.post(url, headers=headers, json=apples)
                r.post(url, headers=headers, json=bananas)
                response5 = r.get(url, headers=headers, params={"cart-id":cart_id})
                cart = response5.json()[str(cart_id)]
                bananas["quantity"] = 8 # Note we are adding bananas to our cart AGAIN so we only update quantity
                del apples["cart-id"]
                del bananas["cart-id"]
                if apples in cart and bananas in cart:
                    count += 1
                    r.delete(url, headers=headers, json={"cart-id":cart_id})
                    response6 = r.get(url, headers=headers, params={"cart-id":cart_id})
                    if response.status_code == 400 and response.json()["status"] == "failure":
                        count += 1
                    else:
                        print("Test case 9 failure")
                else:
                    print("Test case 8 failure")
            else:
                print("Test case 7 failure")
        else:
            print("Test case 6 failure")
    else:
        print("Test case 5 failure")
else:
    print("Test case 4 failure")
    



print(f"Passed {count/9*100}% of test cases")