def test_get(client):
    response = client.get("/")
    assert b"abcd" in response.data


def test_post(client):
    response = client.post("/post_here", data={
        "fruit":"apple"
    })
    assert response.status_code == 200


def test_cli(runner):
    result = runner.invoke(args=["greet"])
    assert "Greetings Flask users all over the world!" in result.output