<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Get Cookie</title>
</head>
<body>
    <%
        Cookie[] cookies = request.getCookies();
        String userName = null;
        if (cookies != null) {
            for (Cookie cookie : cookies) {
                if (cookie.getName().equals("username")) {
                    userName = cookie.getValue();
                    break;
                }
            }
        }
        if (userName != null) {
            out.println("User Name retrieved from cookie: " + userName);
        } else {
            out.println("No User Name found in cookie.");
        }
    %>
</body>
</html>
