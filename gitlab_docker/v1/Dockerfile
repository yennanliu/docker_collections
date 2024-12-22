# Use the official GitLab CE image
FROM gitlab/gitlab-ce:latest

# Expose necessary ports
EXPOSE 80 443 22

# Set default environment variables
ENV GITLAB_OMNIBUS_CONFIG="external_url 'http://localhost';"

# You can add custom commands here if needed, such as configuring GitLab settings or volumes.

CMD ["/assets/wrapper"]