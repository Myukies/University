<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Get Session</title>
</head>
<body>
    <%
        String userName = (String) session.getAttribute("username");
        if (userName != null) {
            out.println("User Name retrieved from session variable: " + userName);
        } else {
            out.println("No User Name found in session variable.");
        }
    %>
</body>
</html>
