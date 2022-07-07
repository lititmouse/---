def just_ip(s):
    list_ip_parts = s.split('.')
    temp = 0
    if len(list_ip_parts) == 4:
        for ip in list_ip_parts:
            if int(ip) >= 0 and int(ip) <= 255:
                pass
            else:
                return "NO"
        return "Yes"    
    return "NO"

                

if __name__ == "__main__":
    x = just_ip(input())
    print(x)
