from locust import HttpUser, task


class WebsiteUser(HttpUser):
    # @task
    # def check_python(self):
    #     # replace with the actual data you want to use for testing
    #     data = {"code": "print('Hello, World!')", "language": "python"}
    #     self.client.post("/syntax-check", json=data, data=data)

    @task
    def check_java(self):
        data = {
            "code": """
package code_syntax_check.test;

import java.util.Map;

class java_code {
    public static void main(String[] args) {
        System.out.println("Start sleeping...");
        try {
            Thread.sleep(1000 * 5);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        Map<String, String> map = Map.of("key", "value")
    }
}
""",
            "language": "java"
        }
        self.client.post("/syntax-check", data=data)

    # @task
    # def check_javascript(self):
    #     data = {"code": "console.log('Hello, World!');",
    #             "language": "javascript"}
    #     self.client.post("/syntax-check", data=data)

    # @task
    # def check_c(self):
    #     data = {
    #         "code": """
    #         #include <stdio.h>
    #         int main() {
    #            printf("Hello World");
    #            return 0;
    #         }""",
    #         "language": "c"
    #     }
    #     self.client.post("/syntax-check", data=data)

    # @task
    # def check_cpp(self):
    #     data = {
    #         "code": """
    #         #include <iostream>
    #         int main() {
    #            std::cout << "Hello World";
    #            return 0;
    #         }""",
    #         "language": "cpp"
    #     }
    #     self.client.post("/syntax-check", data=data)
