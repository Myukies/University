<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Set Cookie</title>
</head>
<body>
    <form action="setCookie.jsp" method="post">
        Enter User Name: <input type="text" name="username">
        <input type="submit" value="Submit">
    </form>

    <%
        String userName = request.getParameter("username");
        if (userName != null && !userName.isEmpty()) {
            Cookie cookie = new Cookie("username", userName);
            cookie.setMaxAge(24 * 60 * 60); // Cookie expiration time (in seconds)
            response.addCookie(cookie);
            out.println("User Name stored in cookie successfully.");
        }
    %>
</body>
</html>
