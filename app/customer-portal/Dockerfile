# Build Stage
FROM node:lts as build

# Install pnpm globally
RUN npm install -g pnpm


WORKDIR /app

# Copy package.json and pnpm-lock.yaml
COPY package*.json pnpm-lock.yaml ./

# Clean node_modules and build directories if they exist
RUN rm -rf node_modules
RUN rm -rf build

# Install dependencies
RUN pnpm install

# Copy the rest of the application
COPY . .

# Build the application with the environment variable
ARG VITE_COMPANY_SEARCH_API
ENV VITE_COMPANY_SEARCH_API=$VITE_COMPANY_SEARCH_API

RUN pnpm run build

# Run Stage
FROM node:lts as run

# Install pnpm globally
RUN npm install -g pnpm

WORKDIR /app

# Copy package.json and pnpm-lock.yaml from the build stage
COPY --from=build /app/package*.json ./
COPY --from=build /app/pnpm-lock.yaml ./

# Copy the built files from the build stage
COPY --from=build /app/build ./build

# Install production dependencies
RUN pnpm install --prod

# Expose the application port
EXPOSE 8080

# Set the default command to run the application
CMD ["sh", "-c", "export PORT=${PORT:-8080} && pnpm start"]
